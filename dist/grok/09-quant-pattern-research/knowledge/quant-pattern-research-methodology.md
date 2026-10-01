# Quant Pattern Research: Methodology

## 1. Returns and statistics
- Daily return r_t = Close_t / Close_(t−1) − 1, using adjusted closes. Excess return = r_stock − r_benchmark.
- Monthly return = compounded daily returns within the calendar month.
- Bucket test: t = mean ÷ (sd ÷ √n). With n ≈ 10 observations per month bucket, a mean needs |t| > 2.26 (df 9, 5% two-tailed). State n honestly.
- Hit rate: % positive. Binomial test vs 50% (or vs the stock's overall hit rate).
- **Multiple testing:** 12 months tested gives about a 46% chance that at least 1 looks "significant" at the 5% level by luck. Apply a Bonferroni (α/12) or Benjamini-Hochberg correction and report both raw and adjusted significance.
- **Stability:** split the sample in halves. A real pattern should appear with the same sign in both halves.
- **After costs:** assume about 5–10 bps round-trip for large caps, plus spread. An edge of under about 20 bps per trade is usually not exploitable.
- **Mechanism:** require a plausible reason (tax-loss selling, index rebalancing, earnings timing, flows, product cycles). With no mechanism and a weak t, call it Noise.

## 2. Event studies (FOMC, CPI, earnings)
- Event dates: FOMC statements from federalreserve.gov; CPI release dates from bls.gov; earnings dates from the company's IR pages or 8-K timestamps.
- Measure the event-day return and absolute return vs non-event days (Welch's t-test). Report the mean |move| ratio (event ÷ normal).
- Earnings: the pre-run window is t−10 to t−1; the gap is the close on the first reaction day vs the prior close (accounting for after-close timing); drift is t+1 to t+20. Split by surprise sign. Report each statistic with n.

## 3. Insider activity (SEC Form 4; OpenInsider, secform4.com, EDGAR)
- Only open-market purchases (code P) are strongly informative. Sales (code S) are often routine (10b5-1 plans, diversification, taxes).
- Signals: cluster buying (3 or more insiders within 30 days), CEO/CFO purchases larger than $100k, buying after a large price decline.
- Grants (code A) and option exercises (code M) are not signals on their own.

## 4. Institutional ownership (13F)
- Filed 45 days after quarter end, so it is stale. Long positions only; no shorts.
- Track: % of shares held by institutions, the number of holders, net shares added, and the top-10 holder changes. Passive index funds are not "smart money"; note the active vs passive mix if possible.

## 5. Short interest and squeeze-potential score (0–10)
Inputs: short % of float (FINRA, published twice a month), days to cover (short interest ÷ average daily volume), borrow fee/utilisation if available, float size, and catalyst proximity.
| Component | 0 | 1 | 2 |
|---|---|---|---|
| Short % float | < 5% | 5–15% | > 15% |
| Days to cover | < 2 | 2–5 | > 5 |
| SI trend (6 months) | Falling | Flat | Rising |
| Borrow cost / utilisation | Low | Moderate | High (> 10% fee / > 90% utilisation) |
| Catalyst + small float | None | One | Both |
0–3 low, 4–6 moderate, 7–10 high. High short interest can also be correct (a bearish fundamental view), so say both sides.

## 6. Options activity
- Put/call volume ratio vs its own 20-day average; IV rank (current IV vs its 52-week range); term structure (event bump around earnings).
- "Unusual activity" means volume much greater than open interest, large block trades, or far-OTM sweeps. Note that you can't distinguish hedges from directional bets, so label it as sentiment and give low predictive confidence.

## 7. Sector rotation / factors
- Relative strength = stock ÷ sector ETF (and ÷ SPY), comparing 3- and 6-month trends.
- Factor sensitivities: regress daily or weekly returns on SPY plus factor proxies (e.g. IWD−IWF for value−growth, TLT for rates, USO for oil, UUP for USD). Report the betas and t-stats when you can compute them; otherwise give a qualitative view tagged EST.
- Business cycle mapping: early cycle (financials, discretionary, industrials), mid (tech, communications), late (energy, materials), recession (staples, healthcare, utilities).

## 8. Edge scorecard verdicts
- **Robust:** adjusted significance, the same sign in both halves, after-cost effect above the threshold, and a mechanism.
- **Weak:** raw significance only, or no mechanism, or unstable across sub-periods.
- **Noise:** not significant. This is the most common honest result, and reporting it is fine.

## 9. Code template (Python, when the platform can run code)
Load the CSV → parse dates → compute adjusted returns → groupby month and weekday → scipy.stats ttest_1samp / ttest_ind → split into halves for stability → output tables. Print n for every bucket.
