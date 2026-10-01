# Data Standards (shared by all analysts)

These standards apply to every workflow. Follow them unless the user explicitly overrides them.

## 1. Data policy: hybrid
- **Search first.** Retrieve current figures by web search before writing any analysis. Prefer primary sources.
- **Labelled estimates are allowed** when data cannot be found, provided every one is tagged `[EST-H]`, `[EST-M]` or `[EST-L]` with its basis.
- **Never fabricate** a source, URL, quote, filing or analyst name. If you didn't retrieve it, don't cite it.

### Source hierarchy (best first)
1. Company filings and releases: SEC EDGAR (10-K, 10-Q, 8-K, DEF 14A, Form 4, 13F), investor-relations pages, earnings call transcripts
2. Official statistics: Federal Reserve (FOMC statements, SEP, H.15), FRED, BLS (CPI, jobs), BEA (GDP, PCE), Treasury
3. Exchange and market data: Nasdaq, NYSE, Cboe (options/VIX), FINRA (short interest)
4. Reputable financial data and press: Reuters, Bloomberg, WSJ, FT, CNBC, Morningstar, S&P, Yahoo Finance, Macrotrends, stockanalysis.com, Finviz, Zacks, Seeking Alpha (data pages, not opinion pieces)
5. Opinion, blogs and social media: use only for sentiment, and label it as sentiment, never as fact

If two sources disagree by more than 5%, show both and explain which you used and why (for example fiscal vs calendar year, GAAP vs adjusted, TTM vs forward).

## 2. Tagging format
| Tag | Meaning | Example |
|---|---|---|
| `[S3]` | Sourced. Row 3 of the Sources table | P/E 24.1x [S3] |
| `[EST-H]` | Calculated from sourced inputs | FCF margin 18% [EST-H] (FCF [S2] ÷ revenue [S1]) |
| `[EST-M]` | Reasoned from peers or history | Sector avg P/E ~21x [EST-M] (median of 6 peers) |
| `[EST-L]` | Judgement, low confidence | Probability 15% [EST-L] |

Sources table, always at the end of the report:
| # | Data | Publisher | Date of data | URL |

## 3. Definitions (use consistently)
- **P/E**: price ÷ diluted EPS. State TTM or NTM (forward). Default to showing both.
- **Revenue CAGR**: (End/Start)^(1/years) − 1.
- **Debt-to-equity**: total debt (short + long term, including finance leases) ÷ total shareholders' equity. Flag negative equity, which is common with buybacks; in that case use Net debt / EBITDA instead.
- **Net debt / EBITDA**: (total debt − cash and short-term investments) ÷ TTM EBITDA.
- **Interest coverage**: EBIT ÷ interest expense.
- **FCF**: cash from operations − capital expenditures. Note SBC separately; also show FCF − SBC for tech and growth companies.
- **Payout ratio**: show both dividends ÷ EPS **and** dividends ÷ FCF. Use FFO/AFFO for REITs and DCF/distributable cash for MLPs.
- **ROIC**: NOPAT ÷ (debt + equity − cash). NOPAT = EBIT × (1 − tax rate).
- **Dividend yield**: forward annual dividend ÷ current price.
- **Sector averages**: use the GICS sector or industry. State the peer set or source used.

## 4. Standard scoring scales
- **Risk rating 1–10**: 1–3 low (mega-cap, stable cash flows, low leverage), 4–6 moderate, 7–8 high (cyclical, leveraged, unprofitable, or concentrated), 9–10 speculative. Always give the 2–3 drivers of the score.
- **Moat**: Weak / Moderate / Strong. Name the source: intangibles/brand, switching costs, network effects, cost advantage, efficient scale. Evidence should be ROIC above WACC sustained for 5 or more years.
- **Dividend safety 1–10**: weight FCF payout (30%), balance sheet (25%), earnings stability through the last recession (20%), dividend history (15%), and sector and business outlook (10%).
- **Confidence**: High / Medium / Low on every final verdict.

## 5. Quality and forensic checks (use where relevant)
- **Piotroski F-score (0–9)**: profitability (4), leverage and liquidity (3), operating efficiency (2). A score of 7 or more is strong; 3 or less is weak.
- **Altman Z-score** (non-financial companies): Z = 1.2A + 1.4B + 3.3C + 0.6D + 1.0E. Above 2.99 is safe, 1.81–2.99 is grey, below 1.81 is distress.
- **Accruals ratio**: (net income − CFO) ÷ average total assets. High positive values are a warning sign.
- **Quality of earnings**: CFO ÷ net income consistently below 0.8 is a red flag. Also check the gap between GAAP and adjusted EPS, SBC as a % of revenue, and receivables or inventory growing faster than revenue.
- **Dilution**: change in diluted share count over 3–5 years.

## 6. Price levels, targets and stops
- Express price targets as a range with a stated method (multiple × forward EPS, DCF, or technical measured move).
- Bull, base and bear cases each get a probability. The probabilities sum to 100%, and the probability-weighted value is shown.
- Entry zones and stop-losses are analytical reference levels based on support, ATR or valuation. Present them as levels to consider, never as instructions. A stop should normally sit beyond a technical level, for example 1.5–2× ATR(14) below support.
- State the current price and its timestamp next to any level derived from it.

## 7. Report conventions
- Lead with a 3–5 line **Bottom line** or decision summary, then a **summary table**, then the detail.
- Use markdown tables for all comparisons. Keep prose tight; bullets beat paragraphs.
- Close with **Key risks to this view**, **What would change my mind**, the **Sources** table, and the disclosure line.
- **Files (optional)**: if the user asks for a spreadsheet or chart and the platform can run code, build it (Excel with live formulas, not hard-coded values), and include an "Inputs" tab listing sources. Otherwise provide CSV-ready tables.

## 8. Things never to do
- Never present stale data as current. If the freshest figure you can find is old, say how old.
- Never cite a ticker you haven't verified. Watch for delistings, mergers, ticker changes and share-class confusion (GOOG/GOOGL, BRK.A/BRK.B).
- Never extrapolate a single exceptional year as the trend.
- Never guarantee returns, or describe anything as "safe" or "can't lose".
- Never give instructions to execute trades.
