# 🌊 Ocean Wave — 9-Factor Trend Visualization

> **See the market in 5 seconds, not 5 minutes.**

Ocean Wave is an open-source trend visualization indicator that fuses 9 technical indicators into colored zones (green/yellow/red). It's designed for speed of understanding, not prediction.

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
2. Copy the contents of `pine/ocean-wave-v1.pine`
3. Paste into Pine Editor
4. Click "Add to chart"
5. Configure inputs (MA periods, RSI thresholds, etc.)

### Lite Version (Zones Only)

1. Open TradingView → Pine Editor
2. Copy the contents of `pine/ocean-wave-lite-v1.pine`
3. Paste into Pine Editor
4. Click "Add to chart"
5. Clean chart with just colored zones + MAs

## 📁 Repository Structure

```
ocean-wave-indicator/
├── README.md (this file)
├── LICENSE (Mozilla Public License 2.0)
├── pine/
│   ├── ocean-wave-v1.pine       # Full 9-factor indicator
│   ├── ocean-wave-lite-v1.pine  # Lite zone-only indicator
│   └── CHANGELOG.md
├── python/
│   ├── nonuple_algorithm.py      # Reference Python implementation
│   └── validate_pine_csv.py      # Validation script (offline)
├── backtest/
│   └── results/                  # Backtest data (JSON)
└── docs/
    ├── algorithm.md               # Detailed algorithm description
    └── backtest-results.md        # Full backtest results
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

Contributions welcome! Areas of interest:
- Algorithm improvements (without overfitting)
- Additional indicator combinations
- Multi-timeframe analysis
- Backtesting on more tickers and time periods
- UI/UX improvements for TradingView

## 📄 License

Mozilla Public License 2.0 — use freely, modify, share. Attribution appreciated.

## 🔗 Links

- [Ocean View App](https://yaroslavmak1995-prog.github.io/ocean-view-app/) — Web dashboard
- [TradingView](https://www.tradingview.com/) — Install indicator (coming soon)
- [Algorithm Documentation](docs/algorithm.md)
- [Validation Script](python/validate_pine_csv.py) — Offline Pine Script validation

---

Built with ❤️ by the Ocean View team. Not financial advice. DYOR.