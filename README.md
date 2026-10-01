# Professional Investment Analysis: AI Analyst Suite

Eleven research assistants modelled on the workflows professional investment firms use. Each is set up natively for **Claude, ChatGPT, Gemini, Microsoft Copilot and Grok**.

| # | Assistant | What it produces |
|---|---|---|
| 00 | **Investment Desk** (router) | Triages your question, runs the right workflow, or chains several together (e.g. competitive check → DCF → technical entry) |
| 01 | Stock Screener | Top-10 screening report: P/E vs sector, 5-year revenue, D/E, dividend safety, moat, bull/bear targets, risk 1–10, entry/stop |
| 02 | DCF Valuation | Valuation memo: 5-year FCF build, WACC, terminal value two ways, sensitivity tables, reverse DCF, verdict |
| 03 | Portfolio Risk Assessment | Risk report with heat map: correlation, concentration, rates, FX, stress tests, liquidity, tail risks, hedges, rebalancing |
| 04 | Earnings Preview | Pre-earnings brief: beat/miss history, consensus, KPIs, guidance, implied move, scenarios, buy-before/sell-before/wait |
| 05 | Portfolio Builder | Investment policy document: allocation, ETFs, core/satellite, return and drawdown, rebalancing, tax location, DCA, IPS |
| 06 | Technical Analysis | Report card: multi-timeframe trend, S/R, MAs, RSI/MACD/Bollinger, volume, patterns, Fibonacci, trade plan, rating |
| 07 | Dividend Income Portfolio | Blueprint: 15–20 dividend stocks, safety scores, payout flags, monthly income, 10-year DRIP, tax notes |
| 08 | Competitive Landscape | Consulting-style deck: peers, margins, moats, share, management, R&D, threats, SWOT, best pick, catalysts |
| 09 | Quant Pattern Research | Quant memo: seasonality, day-of-week, FOMC/CPI, insiders, 13F, short interest, options, earnings drift, with significance tests |
| 10 | Macro Impact Briefing | Executive briefing: rates, inflation, GDP, USD, jobs, Fed path, global risks, sector rotation, action plan, timeline |

**Built-in standards (all assistants):** US market and tax rules · hybrid data policy (every figure is tagged as either sourced `[S#]` or a labelled estimate `[EST-H/M/L]`) · math shown · ranges instead of false precision · a self-check before answering · educational-research disclosure.

---

## 1. Fill in your profile (once)
1. Edit [shared/investor-profile.md](shared/investor-profile.md). Leave blank anything you'd rather be asked about each time.
2. Rebuild so every platform package includes it:
   ```bash
   python3 scripts/build.py --install-claude-code
   ```
   (`--install-claude-code` also refreshes this project's `.claude/skills`. Drop the flag if you don't use Claude Code here.)

The profile is uploaded to every platform you configure. Use ranges instead of exact figures if you prefer.

---

## 2. Platform setup
Everything you paste or upload is in `dist/<platform>/<nn-assistant>/`:
- `setup.md`: every field to fill, ready to copy (name, description, instructions, starters, capabilities)
- `instructions.txt`: the same instructions as a plain file
- `knowledge/`: the files to upload (methodology, data standards, your profile)

### Claude (claude.ai and Claude Code)
- **claude.ai:** Settings → Capabilities → turn on **Code execution and file creation**, then Skills → **Upload skill** → choose a zip from `dist/claude/zips/`. Upload all 11. Claude loads the right skill automatically from your request; the Investment Desk hands off to the others.
- Turn on **web search** in chats where you use them.
- **Claude Code:** already installed in `.claude/skills/` for this project. To use them in every project, copy the folders from `dist/claude/skills/` into `~/.claude/skills/`.

### ChatGPT (Custom GPTs; requires a paid plan to create)
For each of the 11 folders in `dist/chatgpt/`:
1. Explore GPTs → **Create** → **Configure** tab.
2. Paste Name, Description, Instructions and Conversation starters from `setup.md`.
3. Upload the 3 files in `knowledge/`.
4. Capabilities: **Web Search ON**, **Code Interpreter & Data Analysis ON**.
5. Save as **Only me**. If you share publicly, review OpenAI's usage policies for financial content first.

Tip: in any chat, type `@` to call another of your GPTs mid-conversation (e.g. `@DCF Valuation`).

### Gemini (Gems, which are becoming Skills)
Google is replacing Gems with **Skills** from **17 Nov 2026** (Workspace accounts from March 2027). Existing Gems migrate automatically, so either route works:
- **Gem (now):** gemini.google.com → Gems → **New Gem** → paste Name and Instructions from `dist/gemini/<nn>/setup.md`, then add the `knowledge/` files (limit: 10 files per Gem; each assistant uses 3).
- **Skill (after the switch):** in Gemini, ask *"Create a skill called <Name> with these instructions:"*, paste the instructions, and attach the knowledge files. Invoke it with `/<skill-name>`. Skills can be stacked, e.g. `/competitive-landscape` then `/dcf-valuation`.

### Microsoft Copilot
- **Microsoft 365 Copilot (work account):** Copilot → **Create agent** → Configure. Paste Name, Description, Instructions (8,000-character limit; all of these fit) and Starter prompts. Upload the `knowledge/` files. Turn on **web search** and **Code interpreter**.
- **Free / consumer Copilot** (no custom agents): open `instructions.txt`, paste it as your first message followed by `My request: …`, and attach the knowledge files. You'll need to do this once per conversation.

### Grok
grok.com → **Projects** → **New Project** (one per assistant) → paste the Instructions from `dist/grok/<nn>/setup.md` and add the `knowledge/` files. Use **DeepSearch** for multi-company work (screener, competitive landscape, macro). The instructions tell Grok to use X posts only as labelled sentiment, never as financial data.

---

## 3. Getting the best results
- **Start with the Investment Desk** if you're unsure which workflow fits. It can chain workflows into a pipeline.
- **Technical Analysis and Quant Pattern Research are far more accurate with real price data.** Download a daily OHLCV CSV (Yahoo Finance → Historical Data → Download, or stooq.com) and upload it. On Claude and ChatGPT the assistant computes the indicators and statistics in code instead of relying on scraped values.
- **Check the `[EST-…]` tags.** Anything tagged `EST-L` is judgement. The Sources table at the end lets you verify the rest.
- **Ask for files:** "build this as an Excel model" (DCF, risk heat map, DRIP projection) works on Claude and ChatGPT.
- **Re-run, don't reuse.** Prices, consensus and macro data go stale fast, so re-run analyses before acting.

## 4. Limitations (read once)
- AI web search is not a Bloomberg terminal. Consensus estimates, options data, short interest and 13F data may be delayed, paywalled or incomplete. The assistants are told to say so rather than guess, but always verify key numbers.
- Price targets, probabilities and stop levels are analytical scenarios, not predictions or instructions.
- These tools produce **educational research, not personalised financial advice.** For decisions with real tax or financial consequences, consider a licensed adviser or a tax professional.

---

## 5. Editing the assistants
Edit the source files, never `dist/`, then rebuild:
```
analysts/<nn-name>/meta.json        name, descriptions, starters
analysts/<nn-name>/instructions.md  core workflow (kept under 8,000 chars per platform)
analysts/<nn-name>/methodology.md   formulas, rubrics, templates (uploaded as knowledge)
shared/core-rules.md                rules inlined into every assistant
shared/data-standards.md            shared definitions & scoring scales (knowledge file)
platforms/<platform>.md             per-platform tool guidance
scripts/build.py                    generator; prints a character-count table and fails if a limit is exceeded
```
Placeholders like `{{METHODOLOGY}}` are filled in per platform. On Claude they become `references/…` paths; elsewhere they name the uploaded knowledge file.
