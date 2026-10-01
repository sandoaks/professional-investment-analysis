# DCF Valuation: Methodology

## 1. When a DCF is the wrong tool
Say so, and use the substitute below (or blend it in):
| Company type | Better method |
|---|---|
| Banks and insurers | Dividend discount / excess return model, P/TBV vs ROE |
| REITs | NAV, P/AFFO |
| Pre-profit biotech | Risk-adjusted NPV by pipeline asset |
| Deep cyclicals at peak or trough earnings | Normalised mid-cycle margins; EV/EBITDA on mid-cycle figures |
| Negative FCF, high growth | Longer horizon (10 years), with an explicit path to target margins |

## 2. Revenue build
- Years 1–2: consensus (state the source and number of analysts). Adjust only with a stated reason.
- Years 3–5: fade linearly from the year-2 growth rate toward the terminal rate plus 1–3%.
- Sanity checks: implied year-5 revenue vs total addressable market; implied market share; does growth exceed the 5-year historical CAGR without a catalyst?
- Scenarios: Bull = consensus high plus slower fade. Bear = consensus low, or a recession year in year 1–2, then recovery.

## 3. Margins
- Use the 5-year average EBIT margin and its trend. Note operating leverage (incremental margins).
- Reconcile with management's long-term targets and peer medians. Expansion of more than 300bp needs a named driver (mix, scale, pricing).

## 4. Free cash flow
UFCF = EBIT × (1 − tax) + D&A − capex − ΔNWC
- Tax: use the effective rate, normalised toward 21% federal plus state (about 24–25%) unless there is a structural reason not to.
- Capex: maintenance capex ≈ D&A for mature firms; growth capex is tied to revenue growth (capex/sales history).
- ΔNWC: NWC as % of revenue (history) × change in revenue.
- SBC: deduct it (it is a real cost). Alternatively, keep it in FCF and use the forward diluted share count with expected dilution. Never do both, or neither.

## 5. WACC
- Rf = current 10-year US Treasury yield (cite the H.15 or Treasury page with a date).
- ERP: 4.5–5.5%. Name the source (Damodaran's implied ERP is the standard reference) and the value used.
- Beta: 5-year monthly vs S&P 500. Blume-adjusted = 0.67 × raw + 0.33. If the company's own beta is noisy, use the median unlevered peer beta, relevered at the target D/E.
- Ke = Rf + β × ERP (+ size premium only for under $2B market cap; state it).
- Kd = YTM on the company's bonds, or interest expense ÷ average debt. After-tax Kd = Kd × (1 − t).
- Weights: equity at market cap, debt at book value (an acceptable proxy), including operating leases if they are material.
- Typical sanity range for a large-cap US company: 7–10%. Explain anything outside it.

## 6. Terminal value
- Perpetuity: TV = UFCF₅ × (1 + g) ÷ (WACC − g). g is 2–3%; it should never exceed long-run nominal GDP (about 4%) or WACC.
- Exit multiple: TV = EBITDA₅ × multiple (peer median NTM EV/EBITDA, or the company's 10-year median, adjusted toward the sector mean).
- Cross-checks: implied exit multiple from the perpetuity TV; implied g from the multiple TV. A 3% g implying a 25x EBITDA multiple is a contradiction; flag it.
- TV share of EV: if it is above 75%, note that the value depends mostly on long-run assumptions.
- Blend: 50/50 by default. Weight the method with the more defensible cross-check more heavily, and state the weights.

## 7. Discounting and bridge
- Mid-year convention: discount factor = 1 ÷ (1 + WACC)^(t − 0.5). Discount TV at t = 5 (end of year), or 4.5 if consistent with the Gordon formula; state which.
- EV − total debt − leases (if included in WACC) − minority interest − preferred + cash and investments + non-operating assets = equity value.
- ÷ diluted shares (treasury method for options/RSUs) = value per share.

## 8. Sensitivity tables
Table A: rows WACC (base −1.0, −0.5, base, +0.5, +1.0); columns g (base −1.0, −0.5, base, +0.5, +1.0).
Table B: rows WACC; columns exit multiple (base −4x, −2x, base, +2x, +4x).
Mark the base cell, and shade cells above the current price vs below it (or use ▲/▼ in markdown).

## 9. Reverse DCF
Hold margins, WACC and TV method at base values. Solve for the constant 5-year revenue CAGR that makes value per share equal to the current price. Interpret it: "The market implies X% CAGR vs Y% historical and Z% consensus."

## 10. Verdict rules
| Price vs base value | Verdict |
|---|---|
| > 15% below | Undervalued |
| within ±15% | Fairly valued |
| > 15% above | Overvalued |
Lower the confidence if the TV is more than 75% of EV, the sensitivity range is wider than ±40%, or there are many [EST-L] inputs.

## 11. Model breakers (rank by $/share impact)
Typical candidates: terminal growth, margin path, WACC/rates, year 1–2 growth, capex intensity, SBC/dilution, a single customer or product, regulation. For each, show "if X instead of Y → value $Z (−n%)".

## 12. Excel build (when requested)
Tabs: Inputs (all assumptions, blue font), History, Projections (formulas), WACC, Terminal value, Sensitivity (two-way data tables or explicit formulas), Sources. No hard-coded outputs. Every output cell traces back to Inputs.
