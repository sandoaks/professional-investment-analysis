# Stock Screener: Methodology

## 1. Profile → screen criteria map
| Profile input | Conservative (risk 1–3) | Moderate (4–6) | Aggressive (7–10) |
|---|---|---|---|
| Market cap | > $50B | > $10B | > $2B (small caps allowed) |
| Profitability | GAAP profitable 5/5 years | Profitable 4/5 years | FCF positive, or a credible path within 2 years |
| Leverage | Net debt/EBITDA < 2x | < 3x | < 4x, or net cash |
| Interest coverage | > 10x | > 5x | > 3x |
| Valuation | Fwd P/E ≤ sector median | PEG < 2 | PEG < 2.5, or EV/Sales justified by growth |
| Growth | Revenue CAGR > 3% | > 7% | > 15% |
| Dividend | Required, FCF payout < 70% | Optional | Not required |
| Beta (5y monthly) | < 1.0 | < 1.3 | Any |
| Liquidity | Avg $ volume > $50M/day | > $20M/day | > $5M/day |

Time horizon: under 3 years → weight valuation and balance sheet more heavily. More than 10 years → weight moat and reinvestment runway more heavily.

Hard filters for every profile: no OTC or pink-sheet listings, no pending acquisition targets (the price is pinned to the deal), no going-concern warnings, and no SPACs unless the user asks.

## 2. Composite score (100 points)
| Factor | Weight | Metrics |
|---|---|---|
| Valuation | 20 | Fwd P/E vs sector median, EV/EBITDA vs 5-year own history, FCF yield |
| Growth | 20 | 5-year revenue CAGR, 3-year EPS CAGR, NTM consensus growth, trend direction |
| Quality | 20 | ROIC (and ROIC − WACC), gross margin stability, Piotroski F-score, CFO/NI |
| Balance sheet | 15 | Net debt/EBITDA, D/E, interest coverage, Altman Z |
| Moat | 10 | Strong = 10, Moderate = 6, Weak = 2 |
| Momentum / revisions | 10 | Price vs 200-day MA, 6-month EPS estimate revisions |
| Profile fit | 5 | Sector preference, dividend preference, beta fit |

Shift the weights by profile: income seekers move 10 points into a Dividend factor (yield, safety, growth); aggressive growth profiles move 10 points from Valuation to Growth. State any reweighting.

## 3. Per-stock profile template
```
### 3. TICKER: Company name (Sector / Industry)
Price $X (date) | Mkt cap $X | Score XX/100 | Risk X/10 | Moat: Strong (switching costs)

**Thesis (2 sentences):** ...
| Metric | Value | Sector / benchmark | Read |
|---|---|---|---|
| P/E TTM / Fwd | | | Cheap / In line / Rich |
| PEG | | | |
| EV/EBITDA | | | |
| Revenue 5y (FY-4 → FY0) | $a → $b → $c → $d → $e | CAGR x% | Accelerating / Steady / Decelerating |
| D/E · Net debt/EBITDA · Coverage | | | Healthy / Watch / Stretched |
| Div yield · FCF payout · Safety | | | x/10 |
| ROIC vs WACC | | | |
| Piotroski F | | | |

**12-month targets:** Bear $X (p%) · Base $X (p%) · Bull $X (p%) → probability-weighted $X (±x% vs price)
Method: e.g. Base = NTM EPS $x × 22x (5-year median P/E)
**Entry zone:** $a–$b (why) · **Stop reference:** $c (why, % below entry)
**Risk X/10 because:** driver 1; driver 2; driver 3
**Red flags:** ... or "none found"
```

## 4. Price target method
- Base = NTM consensus EPS × a justified multiple (5-year median P/E, adjusted for any change in growth or rates).
- Bull = upside EPS (consensus high, or +10–15%) × the upper end of the historical multiple range.
- Bear = downside EPS (consensus low, or −15–25% in a recession) × the trough multiple.
- Default probabilities are 25/50/25. Adjust them, and say why.

## 5. Entry zone and stop logic
- Entry zone: the overlap between valuation support (price at base-case fair value minus a 10–15% margin of safety) and technical support (50- or 200-day MA, prior consolidation). If price is already within the zone, say "within zone".
- Stop reference: below the major support level by 1.5–2× ATR(14), or below the bear-case value for long-term holders. Show the % distance from the top of the entry zone.
- For long-horizon investors, note that a thesis-break condition (for example "gross margin falls below 40% for 2 quarters") is often better than a price stop.

## 6. Sector P/E references
Always fetch current sector P/E from a dated source (for example Yardeni, FactSet Earnings Insight, or an S&P sector page). If you can't find one, compute the median of 5 or more industry peers and tag it [EST-M].

## 7. Portfolio-fit section
- Show the sector count of the top 10, and flag names likely to be highly correlated (same end-market).
- Suggest position-size bands from the profile's max-position rule: risk 1–3 picks up to the max; risk 7+ picks at half the max.
