# Technical Analysis: Methodology

## 1. Indicator formulas (when computing from OHLCV)
- **SMA(n)** = mean of the last n closes. **EMA(n)**: α = 2/(n+1).
- **RSI(14)** (Wilder): avg gain / avg loss with Wilder smoothing; RSI = 100 − 100/(1+RS).
- **MACD** = EMA12 − EMA26; Signal = EMA9 of MACD; Histogram = MACD − Signal.
- **Bollinger Bands(20,2)**: SMA20 ± 2σ(20). %B = (Close − Lower)/(Upper − Lower). Bandwidth = (Upper − Lower)/SMA20.
- **ATR(14)**: Wilder average of the true range = max(H−L, |H−Cprev|, |L−Cprev|).
- **OBV**: running sum of +volume on up-closes and −volume on down-closes.
- **ADX(14)**: above 25 means a trending market; below 20 means range-bound.
- Use adjusted closes (splits/dividends) for the moving averages and raw data for recent levels. Note which you used.

## 2. Plain-English interpretation guide
| Reading | Meaning |
|---|---|
| RSI > 70 | Overbought. In a strong uptrend this can persist; it is not a sell signal on its own |
| RSI < 30 | Oversold. In a downtrend it can persist; look for a bullish divergence |
| RSI 40–50 holding in an uptrend | A healthy pullback zone |
| MACD crosses above signal, below zero | An early bullish momentum shift (lower reliability) |
| MACD crosses above signal, above zero | Trend continuation |
| Price at the upper Bollinger Band with expanding bands | A strong trend, "walking the band" |
| Bandwidth at a 6-month low | A squeeze; a volatility expansion is likely and the direction is unknown |
| Price above a rising 200-day | Primary uptrend |
| Golden cross (50 above 200) | A lagging confirmation; its historical edge is modest |

## 3. Support and resistance
Rank levels by confluence: prior swing highs/lows touched 2 or more times, high-volume nodes, gap edges, the 50/200-day MA, round numbers, and Fibonacci levels. A level with 3 or more confluences is "major". Once broken, support becomes resistance (and vice versa).

## 4. Pattern rules (identify only if the criteria are met)
| Pattern | Criteria | Target |
|---|---|---|
| Head and shoulders (top) | Left shoulder, a higher head, a lower right shoulder; a neckline; volume declining on the right shoulder | Neckline − (head − neckline) |
| Inverse H&S | Mirror image | Neckline + height |
| Cup and handle | A U-shaped base of 7–65 weeks, depth 12–35%, a handle under 15% deep in the upper half | Breakout + cup depth |
| Double top / bottom | Two peaks/troughs within 3%, at least 4 weeks apart | Height projected from the trough/peak |
| Flags / pennants | A sharp pole, then a tight counter-trend consolidation of 1–4 weeks | The pole length projected |
| Ascending / descending triangle | A flat side plus a rising/falling side, with 2+ touches each | Triangle height |
Status must be stated: forming (unconfirmed), confirmed (close beyond the breakout on above-average volume), or failed.

## 5. Fibonacci
Use the most recent major swing (more than 15% move, or the dominant swing on the weekly chart). For an uptrend retracement: level = High − (High − Low) × ratio. The 38.2–61.8% zone is the typical "bounce zone". Note confluence with MAs or prior structure.

## 6. Trade plan math
- Entry: a zone at support confluence (pullback entry) or above resistance after a confirmed close (breakout entry). State the trigger.
- Stop: below the structural support minus 1–1.5× ATR (swing) or 2× ATR (position).
- Targets: T1 = the next resistance; T2 = the measured move or the next major level.
- R:R = (T1 − Entry) ÷ (Entry − Stop). Below 1.5 is a weak setup; 2.0 or above is favourable.
- Position size (if account size is known): shares = (account × 1%) ÷ (Entry − Stop).

## 7. Rating scoring grid
| Category | Weight | +2 / +1 / 0 / −1 / −2 |
|---|---|---|
| Trend (multi-timeframe) | 30% | All up … all down |
| Moving averages | 15% | Above all, rising … below all, falling |
| Momentum (RSI/MACD) | 20% | Strong bullish … strong bearish (account for divergences) |
| Volume / accumulation | 15% | Accumulation … distribution |
| Pattern / structure | 10% | Confirmed bullish … confirmed bearish |
| Risk-reward | 10% | ≥ 3 … < 1 |
Weighted score: ≥ +1.2 Strong Buy; +0.4 to +1.2 Buy; −0.4 to +0.4 Neutral; −1.2 to −0.4 Sell; ≤ −1.2 Strong Sell. Lower the confidence if an earnings report falls within the holding period, or if the timeframes conflict.

## 8. Honesty about TA
Note briefly that technical signals are probabilistic, that many patterns have modest historical edges, and that they work best combined with risk management and fundamentals.
