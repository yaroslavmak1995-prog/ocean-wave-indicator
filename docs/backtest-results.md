# Backtest Results — Ocean Wave v6.1

## Methodology

- **Algorithm**: Nonuple Confirmation v6.1 (9 factors)
- **Period**: 2021-09-29 to 2026-06-18 (5 years)
- **Tickers**: AAPL, TSLA, SPY, GOOGL, NVDA
- **Total trading days**: 5,925 (1,185 per ticker)
- **Test**: Next-day direction prediction (uptrend → price goes up, downtrend → price goes down)

## Results by Ticker

### AAPL
| Metric | Value |
|--------|-------|
| Win Rate | 44.22% |
| Uptrend Win Rate | 52.05% |
| Downtrend Win Rate | 44.88% |
| Neutral Win Rate | 32.17% |
| High Conf Accuracy | 45.58% |
| Low Conf Accuracy | 42.65% |
| Avg Confidence | 55.47% |
| Avg Strength | 58.42% |
| Uptrend Days | 611 |
| Downtrend Days | 459 |
| Neutral Days | 115 |

### TSLA
| Metric | Value |
|--------|-------|
| Win Rate | 46.92% |
| Uptrend Win Rate | 50.51% |
| Downtrend Win Rate | 48.01% |
| Neutral Win Rate | 13.95% |
| High Conf Accuracy | 48.87% |
| Low Conf Accuracy | 44.47% |
| Avg Confidence | 58.69% |
| Avg Strength | 67.84% |
| Uptrend Days | 588 |
| Downtrend Days | 554 |
| Neutral Days | 43 |

### SPY
| Metric | Value |
|--------|-------|
| Win Rate | 45.23% |
| Uptrend Win Rate | 53.58% |
| Downtrend Win Rate | 43.60% |
| Neutral Win Rate | 46.53% |
| High Conf Accuracy | 46.76% |
| Low Conf Accuracy | 43.66% |
| Avg Confidence | 51.80% |
| Avg Strength | 52.37% |
| Uptrend Days | 713 |
| Downtrend Days | 328 |
| Neutral Days | 144 |

### GOOGL
| Metric | Value |
|--------|-------|
| Win Rate | 45.74% |
| Uptrend Win Rate | 52.92% |
| Downtrend Win Rate | 45.84% |
| Neutral Win Rate | 20.69% |
| High Conf Accuracy | 48.50% |
| Low Conf Accuracy | 42.17% |
| Avg Confidence | 56.95% |
| Avg Strength | 60.82% |
| Uptrend Days | 701 |
| Downtrend Days | 397 |
| Neutral Days | 87 |

### NVDA
| Metric | Value |
|--------|-------|
| Win Rate | 44.47% |
| Uptrend Win Rate | 50.92% |
| Downtrend Win Rate | 42.48% |
| Neutral Win Rate | 9.38% |
| High Conf Accuracy | 47.69% |
| Low Conf Accuracy | 40.27% |
| Avg Confidence | 58.33% |
| Avg Strength | 64.37% |
| Uptrend Days | 709 |
| Downtrend Days | 412 |
| Neutral Days | 64 |

## Aggregated Results

| Metric | Average |
|--------|---------|
| **Win Rate** | **45.32%** |
| Uptrend Win Rate | 52.00% |
| Downtrend Win Rate | 44.96% |
| Neutral Win Rate | 24.54% |
| High Conf Accuracy | 47.48% |
| Low Conf Accuracy | 42.64% |
| Avg Confidence | 56.25% |

## Key Findings

1. **45.32% win rate is BELOW RANDOM (50%)** — the algorithm cannot reliably predict market direction
2. **High confidence ≠ high accuracy** — only 5pp difference (47.48% vs 42.64%)
3. **Uptrend predictions are slightly better** (52%) but still not tradable
4. **GOOGL confidence instability**: 0%→87% confidence swing in a single day (Feb 27, 2026)
5. **Neutral predictions are unreliable** (9-47% depending on ticker)

## Confidence Stability Score (CSS)

CSS measures how stable the confidence score is over consecutive bars:

| Ticker | Avg CSS | CSS Higher Accuracy | CSS Lower Accuracy |
|--------|---------|-------------------|-------------------|
| AAPL | 2.71 | 45.88% | 33.94% |
| TSLA | 2.77 | 47.70% | 40.16% |
| SPY | 2.73 | 46.10% | 39.62% |
| GOOGL | 2.74 | 47.01% | 36.73% |
| NVDA | 2.75 | 46.00% | 32.59% |

**Finding**: Higher CSS (more stable confidence) does NOT significantly improve accuracy.

## Conclusion

The Nonuple Algorithm is effective at **identifying trend context** (the direction of the current move) but **cannot predict future direction** with above-random accuracy. Its value lies in **visualization** — helping traders see trend context quickly — not in **prediction**.