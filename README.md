# 🌊 Ocean Wave — 9-Factor Trend Visualization

> **See the market in 5 seconds, not 5 minutes.**

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![GitHub stars](https://img.shields.io/github/stars/yaroslavmak1995-prog/ocean-wave-indicator?style=social)](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/yaroslavmak1995-prog/ocean-wave-indicator)](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/commits)
[![Backtest](https://img.shields.io/badge/Backtest-5y%20%C3%97%205%20tickers-blue)](docs/backtest-results.md)
[![Win Rate](https://img.shields.io/badge/Win%20Rate-45.32%25%20(honest)-orange)](docs/backtest-results.md)

Ocean Wave is an open-source **Pine Script indicator** for TradingView that fuses 9 technical indicators into colored zones (green/yellow/red). It's designed for speed of understanding, not prediction. Now with confidence smoothing and 11 alert conditions (v2.1).

**Keywords:** pine script indicator, trading visualization, trend zones, multi-indicator, RSI + ADX + MACD + Bollinger Bands, TradingView indicator, open source trading tool, trend analysis, market context, confidence score

---

## ⚡ Try It in 30 Seconds

No installation, no signup — just 3 steps:

1. **Open** the [TradingView indicator page](https://www.tradingview.com/script/4ZzTlQct-Ocean-Wave-9-Factor-Trend-Visualization/)
2. **Click** "Add to chart" (free TradingView account required)
3. **See** colored zones — green = uptrend, yellow = neutral, red = downtrend

That's it. You now see 9 indicators at a glance instead of 9 separate charts.

---

> ### ⭐ **Star this repo** — it helps other traders discover Ocean Wave and motivates us to keep building!

---

## ⚠️ DISCLAIMER

**THIS IS A VISUALIZATION TOOL, NOT A SIGNAL SERVICE.**

Based on a 5-year backtest (AAPL, TSLA, SPY, GOOGL, NVDA — 5,925 trading days):

| Metric | Value |
|--------|-------|
| Average Win Rate | **45.32%** (below random 50%) |
| High Confidence Accuracy | 47.48% |
| Low Confidence Accuracy | 42.64% |
| Uptrend Prediction Win Rate | 52.00% |
| Downtrend Prediction Win Rate | 44.96% |

**Key findings:**
- High confidence does NOT improve accuracy significantly (47.48% vs 42.64%)
- The algorithm CANNOT predict market direction reliably
- The VALUE is in visualization — seeing trend context at a glance

Use Ocean Wave to understand market context faster, not to predict price direction.

## 📊 How It Works

### 9 Indicators → 1 Signal

| # | Indicator | What It Measures | Bonus Range |
|---|-----------|-----------------|-------------|
| 1 | MA Crossover (20/50) | Base trend direction | ±15 base |
| 2 | Volume Confirmation | Signal strength | -10 to +15 |
| 3 | Momentum Check | Price vs MA position | -5 to +10 |
| 4 | RSI (14) | Overbought/oversold | -10 to +15 |
| 5 | ADX (14) | Trend strength | -15 to +15 |
| 6 | MACD (12/26/9) | Momentum crossover | -10 to +15 |
| 7 | ATR (14) | Volatility assessment | -15 to +3 |
| 8 | Bollinger Bands (20, 2σ) | Price position, squeeze | -16 to +7 |
| 9 | Stochastic (14/3/3) | Momentum oscillator | -7 to +8 |

**Synergy Bonus:** When 4+ indicators agree → confidence +10

**Confidence Floor:** 3+ confirmations → min 25%, 5+ → min 50%

### Output

- **Zone Color:** Green (uptrend) / Yellow (neutral) / Red (downtrend)
- **Confidence:** 0-100% (how many indicators agree)
- **Strength:** 0-100% (magnitude of trend)
- **Factor Table:** 9 factors with individual values
- **Signal Label:** Trend direction + confidence percentage

## 🚀 Installation (TradingView)

### Full Version (9-Factor with Tables)

1. Open TradingView → Pine Editor
2. Copy the contents of `pine/ocean-wave-v2.1.pine` (latest)
3. Paste into Pine Editor
4. Click "Add to chart"
5. Configure inputs (MA periods, RSI thresholds, smoothing, alerts)

### v2.1 New Features

- ✨ **Confidence Smoothing** — EMA-based smoothing prevents wild confidence jumps
- 🚨 **Zone Change Alerts** — get notified when trend zone changes color
- 📊 **Confidence Threshold Alerts** — alert when confidence crosses your threshold
- 11 total alert conditions (was 6 in v1.1)

### Lite Version (Zones Only)

1. Open TradingView → Pine Editor
2. Copy the contents of `pine/ocean-wave-lite-v2.1.pine` (latest, with smoothing + alerts)
3. Paste into Pine Editor
4. Click "Add to chart"
5. Clean chart with just colored zones + MAs + 8 alert conditions

**Lite v2.1** includes the same confidence smoothing, rate-limiting, zone change alerts, and confidence threshold alerts as Full v2.1. Total alerts: 8 (was 3 in v1.1).

## 📁 Repository Structure

```
ocean-wave-indicator/
├── README.md (this file)
├── LICENSE (Mozilla Public License 2.0)
├── CONTRIBUTING.md              # Contributor guide
├── CODE_OF_CONDUCT.md          # Community standards
├── .github/
│   ├── ISSUE_TEMPLATE/         # Bug report, feature request, backtest templates
│   └── PULL_REQUEST_TEMPLATE.md
├── pine/
│   ├── ocean-wave-v2.1.pine     # Full 9-factor indicator (latest)
│   ├── ocean-wave-lite-v2.1.pine # Lite zone-only indicator (latest)
│   ├── ocean-wave-v1.pine       # Full 9-factor indicator (original)
│   ├── ocean-wave-lite-v1.pine  # Lite zone-only indicator (original)
│   └── CHANGELOG.md
├── python/
│   ├── nonuple_algorithm.py      # Reference Python implementation
│   └── validate_pine_csv.py      # Validation script (offline)
├── backtest/
│   └── results/                  # Backtest data (JSON)
└── docs/
    ├── algorithm.md               # Detailed algorithm description
    ├── architecture.md            # System architecture diagram
    ├── backtest-results.md        # Full backtest results
    └── example-configs.md         # Trading style presets (scalping/swing/position)
```

## 📈 Backtest Results

### 5-Year Backtest (2021-09-29 to 2026-06-18)

| Ticker | Win Rate | Uptrend Win | Downtrend Win | Avg Confidence |
|--------|----------|-------------|---------------|----------------|
| AAPL | 44.22% | 52.05% | 44.88% | 55.47% |
| TSLA | 46.92% | 50.51% | 48.01% | 58.69% |
| SPY | 45.23% | 53.58% | 43.60% | 51.80% |
| GOOGL | 45.74% | 52.92% | 45.84% | 56.95% |
| NVDA | 44.47% | 50.92% | 42.48% | 58.33% |
| **AVG** | **45.32%** | **52.00%** | **44.96%** | **56.25%** |

### Key Findings

1. **45.32% win rate is BELOW RANDOM (50%)** — this algorithm cannot predict market direction
2. **High confidence ≠ high accuracy** — 47.48% vs 42.64% for low confidence (only 5pp difference)
3. **Uptrend predictions are slightly better** (52%) but still not reliable enough for trading
4. **GOOGL confidence can swing 85pp in one day** — algorithm is unstable during high volatility
5. **Neutral predictions are almost always wrong** (9-47% win rate depending on ticker)

## 🧪 Validation

The Pine Script implementation has been validated against the Python Nonuple Algorithm v6.1:

```
AAPL: Trend match 100.0% | Zone match 60.7% | Strength diff 26.6pp | Confidence diff 27.9pp
```

- **Trend direction** matches 100% — the algorithm correctly identifies uptrend/downtrend/neutral
- **Zone and confidence differences** are due to known issues (see CHANGELOG.md)
- Known bug: confidence double-counting (indicators counted 2-3 times) — fix planned for v1.1

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines. Please note that this project follows the [Code of Conduct](CODE_OF_CONDUCT.md).

Areas of interest:
- Algorithm improvements (without overfitting)
- Additional indicator combinations
- Multi-timeframe analysis
- Backtesting on more tickers and time periods
- UI/UX improvements for TradingView
- Documentation and examples (see [example configs](docs/example-configs.md))

## 📄 License

Mozilla Public License 2.0 — use freely, modify, share. Attribution appreciated.

## 🔗 Links

- [Ocean View App](https://yaroslavmak1995-prog.github.io/ocean-view-app/) — Web dashboard
- [TradingView](https://www.tradingview.com/script/4ZzTlQct-Ocean-Wave-9-Factor-Trend-Visualization/) — Install indicator
- [Algorithm Documentation](docs/algorithm.md)
- [Architecture Diagram](docs/architecture.md)
- [Validation Script](python/validate_pine_csv.py) — Offline Pine Script validation

---

Built with ❤️ by the Ocean View team. Not financial advice. DYOR.

## 🔮 Coming Soon (v3)

- 🌐 **Multi-timeframe mode** — see D1 trend zone on H1 chart (Issue #2)
- 📊 **Multi-ticker backtest dashboard** — test multiple tickers at once in the web app (Issue #8)
- ⚙️ **Preset dropdown** — switch between Scalping / Swing / Position presets directly in Pine Script (Issue #10)
- 🔧 **Confidence fix** — address indicator double-counting for more accurate scores
- 📸 **Screenshot gallery** — real examples for different market conditions

⭐ **Star and follow** to get notified when v3 drops!

---

## 📋 Roadmap

We use GitHub Issues to track planned features. Current status:
- ✅ [#1: Alert conditions for trend zone changes](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues/1) — CLOSED, addressed in v2.1
- ✅ [#3: Improve confidence stability](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues/3) — CLOSED, addressed in v2.1
- ✅ [#4: Lite v2.1 with confidence smoothing + zone alerts](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues/4) — CLOSED, Lite v2.1 released
- 🔵 [#2: Multi-timeframe mode (D1 trend on H1 chart)](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues/2) — Planned for v3
- 🔵 [#8: Multi-ticker backtest dashboard for web app](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues/8) — Planned

### 💬 Discussions

We have [GitHub Discussions](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions) enabled! Join the conversation:
- [👋 Welcome & Ask Anything](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions/5)
- [💡 Feature Requests for v3](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions/6)
- [📊 Share Your Backtest Results](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions/7)

Have an idea? [Open an issue](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues/new) or start a [discussion](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions)!