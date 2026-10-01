#!/usr/bin/env python3
"""Build platform-native assistant setups from the analyst source files.

Source of truth:
  analysts/<nn-name>/{meta.json, instructions.md, methodology.md}
  shared/{core-rules.md, data-standards.md, investor-profile.md}
  platforms/<platform>.md   (tooling paragraph inlined into instructions)

Output (dist/ is wiped and regenerated on every run):
  dist/claude/skills/<slug>/...   Claude skill folders
  dist/claude/zips/<slug>.zip     upload to claude.ai
  dist/<platform>/<nn-slug>/      setup.md + knowledge/ for chatgpt, gemini, copilot, grok

Usage:
  python3 scripts/build.py                        # build dist/
  python3 scripts/build.py --install-claude-code  # also copy skills into ./.claude/skills
"""

import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ANALYSTS = ROOT / "analysts"
SHARED = ROOT / "shared"
PLATFORMS = ROOT / "platforms"
DIST = ROOT / "dist"

ROUTER_SLUG = "investment-desk"

# Hard instruction limits per platform (characters). None = no published limit.
LIMITS = {"chatgpt": 8000, "copilot": 8000, "gemini": None, "grok": None, "claude": None}
WARN_MARGIN = 300

PLATFORM_INFO = {
    "chatgpt": {
        "title": "ChatGPT Custom GPT",
        "fields": "Configure tab → Name, Description, Instructions, Conversation starters, Knowledge, Capabilities",
        "capabilities": {"web_search": "Web Search: ON", "code": "Code Interpreter & Data Analysis: ON"},
        "extra_caps": ["Canvas: optional", "Image Generation: OFF"],
        "max_starters": 4,
    },
    "gemini": {
        "title": "Gemini Gem / Skill",
        "fields": "Gem manager → New Gem → Name, Instructions, Knowledge",
        "capabilities": {"web_search": "Google Search grounding is built in", "code": "Code execution: used automatically where available"},
        "extra_caps": [],
        "max_starters": 0,
    },
    "copilot": {
        "title": "Microsoft 365 Copilot agent",
        "fields": "Agent Builder → Configure → Name, Description, Instructions, Knowledge, Capabilities, Starter prompts",
        "capabilities": {"web_search": "Web search (Knowledge → 'Search all websites'): ON", "code": "Code interpreter: ON"},
        "extra_caps": [],
        "max_starters": 6,
    },
    "grok": {
        "title": "Grok Project",
        "fields": "grok.com → Projects → New Project → Name, Instructions, Files",
        "capabilities": {"web_search": "Web search is on by default; use DeepSearch for heavy research", "code": "Code execution: used where available"},
        "extra_caps": [],
        "max_starters": 0,
    },
}


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8").strip() + "\n"


def load_analysts():
    out = []
    for d in sorted(p for p in ANALYSTS.iterdir() if p.is_dir() and re.match(r"\d\d-", p.name)):
        meta = json.loads((d / "meta.json").read_text(encoding="utf-8"))
        meta["dir"] = d
        meta["prefix"] = d.name.split("-", 1)[0]
        meta["instructions"] = read(d / "instructions.md")
        mpath = d / "methodology.md"
        meta["methodology"] = read(mpath) if mpath.exists() else ""
        out.append(meta)
    return out


def refs_for(platform: str, slug: str) -> dict:
    """How each placeholder is phrased on a given platform."""
    if platform == "claude":
        return {
            "METHODOLOGY": "`references/methodology.md`",
            "DATA_STANDARDS": "`references/data-standards.md`",
            "PROFILE": "the user's investor profile (from the conversation, project knowledge, or `references/investor-profile.md` if it has been filled in)",
            "ROUTE_HOW": (
                "each workflow is its own skill (`stock-screener`, `dcf-valuation`, `portfolio-risk-assessment`, "
                "`earnings-preview`, `portfolio-builder`, `technical-analysis`, `dividend-income-portfolio`, "
                "`competitive-landscape`, `quant-pattern-research`, `macro-impact-briefing`). Load the matching skill "
                "and follow its SKILL.md. If it isn't installed, follow the matching chapter of `references/playbook.md`, "
                "which contains every workflow's full instructions and methodology."
            ),
        }
    return {
        "METHODOLOGY": f"the knowledge file `{slug}-methodology.md`",
        "DATA_STANDARDS": "the knowledge file `data-standards.md`",
        "PROFILE": "the knowledge file `investor-profile.md` (or a profile the user gives in chat)",
        "ROUTE_HOW": (
            f"follow the matching chapter of the knowledge file `{ROUTER_SLUG}-playbook.md`, which contains every "
            "workflow's full instructions and methodology."
        ),
    }


def render(text: str, platform: str, slug: str, core: str, tooling: str, overrides=None) -> str:
    refs = refs_for(platform, slug)
    if overrides:
        refs.update(overrides)
    text = text.replace("{{CORE_RULES}}", core.strip()).replace("{{TOOLING}}", tooling.strip())
    # core rules contain placeholders too, so substitute after inlining
    for key, val in refs.items():
        text = text.replace("{{" + key + "}}", val)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", text)
    if leftover:
        raise SystemExit(f"Unresolved placeholders {leftover} for {slug} on {platform}")
    return re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"


def build_playbook(analysts, platform: str, core: str) -> str:
    """All ten workflows in one document, for the router (knowledge-file platforms and Claude fallback)."""
    parts = [
        "# Investment Desk Playbook\n",
        "Each chapter is a complete specialist workflow. The core rules and tooling in the assistant's main "
        "instructions apply to every chapter.\n",
    ]
    for a in analysts:
        if a["slug"] == ROUTER_SLUG:
            continue
        body = render(
            a["instructions"], platform, a["slug"], core="", tooling="",
            overrides={"METHODOLOGY": "the Methodology section of this chapter"},
        )
        body = re.sub(r"^# ", "## ", body, count=1, flags=re.M)
        meth = re.sub(r"^# .*\n", "", a["methodology"], count=1)
        meth = re.sub(r"^## ", "#### ", meth, flags=re.M)
        parts.append(f"\n---\n\n{body.strip()}\n\n### Methodology\n{meth.strip()}\n")
    return "\n".join(parts)


def check_limit(platform: str, slug: str, text: str, report: list):
    n = len(text)
    lim = LIMITS.get(platform)
    status = "ok"
    if lim and n > lim:
        status = f"OVER LIMIT ({lim})"
    elif lim and n > lim - WARN_MARGIN:
        status = f"near limit ({lim})"
    report.append((platform, slug, n, status))


def build_claude(analysts, core, profile, standards, report):
    tooling = read(PLATFORMS / "claude.md")
    skills_dir = DIST / "claude" / "skills"
    zips_dir = DIST / "claude" / "zips"
    skills_dir.mkdir(parents=True)
    zips_dir.mkdir(parents=True)
    for a in analysts:
        slug = a["slug"]
        body = render(a["instructions"], "claude", slug, core, tooling)
        desc = a["skill_description"]
        if len(desc) > 1024:
            raise SystemExit(f"{slug}: skill_description exceeds 1024 chars")
        skill = f"---\nname: {slug}\ndescription: {json.dumps(desc)}\n---\n\n{body}"
        sd = skills_dir / slug
        (sd / "references").mkdir(parents=True)
        (sd / "SKILL.md").write_text(skill, encoding="utf-8")
        (sd / "references" / "data-standards.md").write_text(standards, encoding="utf-8")
        (sd / "references" / "investor-profile.md").write_text(profile, encoding="utf-8")
        if slug == ROUTER_SLUG:
            (sd / "references" / "playbook.md").write_text(build_playbook(analysts, "claude", core), encoding="utf-8")
        else:
            (sd / "references" / "methodology.md").write_text(a["methodology"], encoding="utf-8")
        check_limit("claude", slug, skill, report)
        with zipfile.ZipFile(zips_dir / f"{slug}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(sd.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(skills_dir))


def setup_doc(platform: str, a: dict, instructions: str, knowledge: list) -> str:
    info = PLATFORM_INFO[platform]
    lines = [
        f"# {a['display_name']}: {info['title']} setup",
        "",
        f"Where: {info['fields']}",
        "",
        "## Name",
        "```text",
        a["display_name"],
        "```",
    ]
    if platform in ("chatgpt", "copilot"):
        lines += ["", "## Description", "```text", a["short_description"], "```"]
    lines += [
        "",
        f"## Instructions ({len(instructions):,} characters)",
        "Copy everything inside the block below.",
        "",
        "````markdown",
        instructions.rstrip(),
        "````",
    ]
    if info["max_starters"]:
        lines += ["", "## Conversation starters"]
        lines += [f"- {s}" for s in a["starters"][: info["max_starters"]]]
    lines += ["", "## Knowledge files to upload (from the `knowledge/` folder next to this file)"]
    lines += [f"- `{k}`" for k in knowledge]
    lines += ["", "## Capabilities"]
    lines += [f"- {info['capabilities'][c]}" for c in a.get("capabilities", []) if c in info["capabilities"]]
    lines += [f"- {c}" for c in info["extra_caps"]]
    if platform == "grok" or platform == "gemini":
        lines += ["", "## Example prompts"] + [f"- {s}" for s in a["starters"]]
    return "\n".join(lines) + "\n"


def build_knowledge_platform(platform, analysts, core, profile, standards, report):
    tooling = read(PLATFORMS / f"{platform}.md")
    base = DIST / platform
    for a in analysts:
        slug = a["slug"]
        out = base / f"{a['prefix']}-{slug}"
        kdir = out / "knowledge"
        kdir.mkdir(parents=True)
        instr = render(a["instructions"], platform, slug, core, tooling)
        check_limit(platform, slug, instr, report)
        files = {"data-standards.md": standards, "investor-profile.md": profile}
        if slug == ROUTER_SLUG:
            files[f"{ROUTER_SLUG}-playbook.md"] = build_playbook(analysts, platform, core)
        else:
            files[f"{slug}-methodology.md"] = a["methodology"]
        for name, content in files.items():
            (kdir / name).write_text(content, encoding="utf-8")
        (out / "instructions.txt").write_text(instr, encoding="utf-8")
        (out / "setup.md").write_text(setup_doc(platform, a, instr, sorted(files)), encoding="utf-8")


def install_claude_code():
    target = ROOT / ".claude" / "skills"
    target.mkdir(parents=True, exist_ok=True)
    for sd in sorted((DIST / "claude" / "skills").iterdir()):
        dest = target / sd.name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(sd, dest)
    print(f"Installed Claude Code skills into {target}")


def main():
    analysts = load_analysts()
    core = read(SHARED / "core-rules.md")
    profile = read(SHARED / "investor-profile.md")
    standards = read(SHARED / "data-standards.md")

    if DIST.exists():
        shutil.rmtree(DIST)
    report = []
    build_claude(analysts, core, profile, standards, report)
    for platform in ("chatgpt", "gemini", "copilot", "grok"):
        build_knowledge_platform(platform, analysts, core, profile, standards, report)

    print(f"Built {len(analysts)} assistants for 5 platforms into {DIST.relative_to(ROOT)}/\n")
    cols = ("claude", "chatgpt", "gemini", "copilot", "grok")
    table = {}
    flags = []
    for platform, slug, n, status in report:
        table.setdefault(slug, {})[platform] = n
        if status != "ok":
            flags.append(f"{platform}/{slug}: {n} chars, {status}")
    print("Instruction length (characters):")
    print(f"{'assistant':<28}" + "".join(f"{c:>9}" for c in cols))
    for slug, row in table.items():
        print(f"{slug:<28}" + "".join(f"{row.get(c, 0):>9}" for c in cols))
    for f in flags:
        print("  ! " + f)
    over = any("OVER" in f for f in flags)
    if over:
        print("\nWARNING: some instructions exceed a platform limit. Move detail into methodology.md.")
        sys.exit(1)

    if "--install-claude-code" in sys.argv:
        install_claude_code()


if __name__ == "__main__":
    main()
