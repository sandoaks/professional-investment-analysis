# Portfolio Risk Assessment: Methodology

## 1. Concentration metrics
- Top-1, top-5 and top-10 weights.
- HHI = Σ wᵢ² (weights as decimals). Effective number of holdings = 1 ÷ HHI. Below 10 is concentrated; below 5 is highly concentrated.
- Sector over/underweight vs S&P 500 sector weights (fetch the current weights, and cite them). Any sector more than 2× the benchmark weight, or above 35% of the portfolio, is 🔴.
- Look through ETFs: compute combined exposure, for example a 10% QQQ holding plus 8% direct AAPL gives total AAPL exposure.

## 2. Correlation
- Preferred: 3-year weekly returns. If you can't compute these, use sector/factor proxy correlations (same sector ≈ 0.7–0.85; different cyclical sectors ≈ 0.5–0.7; equities vs long Treasuries ≈ −0.3 to +0.5, which is regime-dependent and has been positive in inflationary periods; gold vs equities ≈ 0–0.2). Tag proxies [EST-M].
- Clusters: group holdings with ρ > 0.7. Effective independent bets ≈ number of clusters weighted by cluster weight.
- Explain in plain English that diversification falls in a crisis because correlations rise toward 1.

## 3. Geographic and currency exposure
- Use company revenue by region (from 10-K segment notes) for large holdings. Use the fund region mix for ETFs.
- USD strengthening hurts US multinationals with high foreign revenue, and hurts unhedged foreign holdings in USD terms.

## 4. Rate sensitivity rubric
| High | Medium | Low |
|---|---|---|
| Long-duration growth with no profits, REITs, utilities, long bonds (duration > 10), highly leveraged firms with floating or near-term maturities | Quality growth, homebuilders, small caps | Short-duration value, energy, staples with low debt, T-bills, banks (mixed: NIM vs credit) |
For bonds: price change ≈ −duration × Δyield.

## 5. Stress scenarios
| Scenario | S&P 500 peak-to-trough | Notes for proxies |
|---|---|---|
| 2008 GFC (Oct 2007 – Mar 2009) | about −55% | Financials −80%, Discretionary −60%, Staples −30%, long Treasuries +20–25%, gold about +5% |
| 2020 COVID (Feb – Mar 2020) | about −34% | Energy −60%, Tech −30%, Staples −25%; fast recovery |
| 2022 rate shock (Jan – Oct 2022) | about −25% | Nasdaq −35%, long Treasuries −30%+, Energy +40%; stocks and bonds fell together |
| Mild recession (generic) | −20% | Beta-scaled; defensives −10%, cyclicals −30% |
Verify the scenario figures with search where possible. Use the actual historical drawdown of a holding when it existed; otherwise use β × index move, adjusted by sector. Show the top 3 loss contributors per scenario. Recovery time: cite the index history (2008 about 4 years to regain the high; 2020 about 5 months; 2022 about 2 years).

## 6. Liquidity
- Days to liquidate = position $ ÷ (20% of average daily $ volume). More than 1 day is 🟡; more than 5 days is 🔴 (rare for retail investors, except in microcaps).
- Also 🟡/🔴: wide spreads (> 0.5%), interval funds, private assets, thinly traded ETFs, crypto at weekends.

## 7. Position sizing
- Flag any position above the profile maximum (default 10%), or any single stock above 5% for conservative profiles.
- Volatility-aware size: target weight ∝ 1 ÷ volatility, scaled so each name contributes a similar risk. Show the band (min to max %).
- Concentrated legacy positions (low cost basis): mention gradual trimming, exchange funds, collars, or charitable gifting as possibilities, and note that the tax specifics need a tax professional.

## 8. Tail scenarios (pick the 3–5 most relevant to these holdings)
Examples: AI capex bust; sharp rate spike (10-year > 6%); USD crisis; Taiwan/geopolitical supply shock; private credit or bank stress; oil spike > $130; regulatory or antitrust hit to mega-caps; stagflation. For each: probability over 12 months [EST-L] with reasoning, portfolio impact %, and 2–3 leading indicators to watch.

## 9. Hedging menu
| Risk | Low-cost structural fix | Instrument hedge (cost / trade-off) |
|---|---|---|
| Equity beta | Raise bonds/cash weighting | SPY/QQQ put spreads 3–6 months out (about 1–3% of notional); collars (give up upside) |
| Concentration | Trim and diversify | Protective put on the single name; collar |
| Rates | Shorten duration; add floating rate | Short-duration Treasuries, TIPS |
| Inflation | Add real assets | TIPS, commodities, energy, gold |
| USD | Add international exposure | Currency-hedged or unhedged international ETFs, depending on direction |
If the profile says no options, list only non-option hedges.

## 10. Rebalancing
- Targets must reconcile to 100%. Show current %, target %, Δ%, and Δ$.
- Execution order: rebalance inside tax-advantaged accounts first, direct new contributions to underweights, harvest losses in taxable accounts, and avoid short-term gains where possible. Watch the wash-sale rule (30 days).
- Bands: rebalance when a holding drifts ±5 percentage points (absolute) or ±20% (relative) from target.

## 11. Overall risk score (1–10)
Combine: concentration (25%), stress drawdown vs the profile's maximum tolerable drop (25%), correlation/effective bets (20%), leverage and quality of holdings (15%), liquidity and FX (15%). If the stress drawdown exceeds the stated tolerance, state it in bold at the top.
