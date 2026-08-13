# Regime-Segmented Backtest Results

**Date:** 2026-08-13 19:01
**Method:** Split 5-year backtest by market regime (wallneradam's advice)

## Regimes Analyzed

- **Post-COVID Bull Run** (2021-07–2021-12): Strong uptrend, low volatility, QE-driven
- **2022 Bear Market** (2022-01–2022-10): Fed tightening, high inflation, significant drawdowns
- **2022-2023 Recovery** (2022-10–2023-12): Bottoming and gradual recovery, mixed signals
- **2024 Bull Run** (2024-01–2024-12): Strong bull market, AI-driven rally
- **2025-2026 Recent** (2025-01–2026-06): Most recent period, mixed regime

## Results by Ticker and Regime

### AAPL

| Regime | Type | Days | Win% | Up% | Down% | HiConf% | AvgConf |
|--------|------|------|------|-----|-------|---------|---------|
| Post-COVID Bull Run | bull | 46 | 43.48% | 64.71% | 40.91% | 47.62% | 46.78% |
| 2022 Bear Market | bear | 178 | 38.76% | 38.36% | 45.74% | 40.96% | 48.61% |
| 2022-2023 Recovery | recovery | 283 | 41.7% | 51.01% | 38.05% | 42.31% | 64.86% |
| 2024 Bull Run | bull | 232 | 52.59% | 61.11% | 55.26% | 53.64% | 50.98% |
| 2025-2026 Recent | mixed | 353 | 42.21% | 50.86% | 42.96% | 45.68% | 48.47% |

### TSLA

| Regime | Type | Days | Win% | Up% | Down% | HiConf% | AvgConf |
|--------|------|------|------|-----|-------|---------|---------|
| Post-COVID Bull Run | bull | 46 | 60.87% | 60.87% | 0% | 61.54% | 86.02% |
| 2022 Bear Market | bear | 178 | 44.94% | 50.0% | 47.0% | 47.17% | 60.05% |
| 2022-2023 Recovery | recovery | 283 | 47.35% | 51.89% | 47.06% | 50.94% | 60.12% |
| 2024 Bull Run | bull | 232 | 47.84% | 48.39% | 49.51% | 50.42% | 57.43% |
| 2025-2026 Recent | mixed | 353 | 45.04% | 49.43% | 47.24% | 46.03% | 54.61% |

### SPY

| Regime | Type | Days | Win% | Up% | Down% | HiConf% | AvgConf |
|--------|------|------|------|-----|-------|---------|---------|
| Post-COVID Bull Run | bull | 46 | 39.13% | 59.09% | 26.67% | 40.0% | 45.79% |
| 2022 Bear Market | bear | 178 | 42.7% | 39.34% | 50.98% | 44.3% | 47.95% |
| 2022-2023 Recovery | recovery | 283 | 39.22% | 48.7% | 40.43% | 40.83% | 42.95% |
| 2024 Bull Run | bull | 232 | 48.71% | 58.85% | 21.74% | 48.12% | 59.18% |
| 2025-2026 Recent | mixed | 353 | 47.31% | 56.48% | 39.19% | 48.44% | 52.73% |

### GOOGL

| Regime | Type | Days | Win% | Up% | Down% | HiConf% | AvgConf |
|--------|------|------|------|-----|-------|---------|---------|
| Post-COVID Bull Run | bull | 46 | 30.43% | 41.67% | 30.77% | 26.67% | 31.12% |
| 2022 Bear Market | bear | 178 | 40.45% | 34.15% | 49.57% | 44.74% | 45.81% |
| 2022-2023 Recovery | recovery | 283 | 41.7% | 51.52% | 40.86% | 40.5% | 43.22% |
| 2024 Bull Run | bull | 232 | 50.43% | 60.0% | 34.92% | 53.24% | 61.16% |
| 2025-2026 Recent | mixed | 353 | 50.42% | 53.75% | 51.61% | 51.87% | 74.74% |

### NVDA

| Regime | Type | Days | Win% | Up% | Down% | HiConf% | AvgConf |
|--------|------|------|------|-----|-------|---------|---------|
| Post-COVID Bull Run | bull | 46 | 43.48% | 53.12% | 20.0% | 50.0% | 54.28% |
| 2022 Bear Market | bear | 178 | 40.45% | 29.27% | 46.97% | 41.12% | 62.5% |
| 2022-2023 Recovery | recovery | 283 | 42.4% | 50.0% | 28.33% | 45.7% | 65.64% |
| 2024 Bull Run | bull | 232 | 50.43% | 56.98% | 41.03% | 53.96% | 61.72% |
| 2025-2026 Recent | mixed | 353 | 43.91% | 52.54% | 44.37% | 50.0% | 51.98% |

## Combined Regime Analysis

| Regime | AAPL | TSLA | SPY | GOOGL | NVDA | AVG |
|--------|------|------|-----|-------|------|-----|
| Post-COVID Bull Run | 43.5% | 60.9% | 39.1% | 30.4% | 43.5% | 43.5% |
| 2022 Bear Market | 38.8% | 44.9% | 42.7% | 40.5% | 40.5% | 41.5% |
| 2022-2023 Recovery | 41.7% | 47.4% | 39.2% | 41.7% | 42.4% | 42.5% |
| 2024 Bull Run | 52.6% | 47.8% | 48.7% | 50.4% | 50.4% | 50.0% |
| 2025-2026 Recent | 42.2% | 45.0% | 47.3% | 50.4% | 43.9% | 45.8% |

## Consistency Analysis

- **Post-COVID Bull Run:** avg=43.5%, std=9.9%, spread=30.4pp → BELOW 45% — CONSISTENTLY POOR
- **2022 Bear Market:** avg=41.5%, std=2.1%, spread=6.2pp → BELOW 45% — CONSISTENTLY POOR
- **2022-2023 Recovery:** avg=42.5%, std=2.7%, spread=8.1pp → BELOW 45% — CONSISTENTLY POOR
- **2024 Bull Run:** avg=50.0%, std=1.6%, spread=4.8pp → 45-55% — NO CLEAR EDGE
- **2025-2026 Recent:** avg=45.8%, std=2.9%, spread=8.2pp → 45-55% — NO CLEAR EDGE
