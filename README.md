# 🌊 Ocean Wave — Trend Visualizer

> **See the market like ocean waves.**

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)
[![GitHub stars](https://img.shields.io/github/stars/yaroslavmak1995-prog/ocean-wave-indicator?style=social)](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/yaroslavmak1995-prog/ocean-wave-indicator)](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/commits)
[![Version](https://img.shields.io/badge/Version-3.2%20%F0%9F%8C%8A-cyan)](pine/ocean-wave-v3.2.pine)

Ocean Wave turns price action into flowing ocean waves. No patterns to learn. No signals to chase. Just the natural rhythm of the market, visualized. 9 technical factors fused into 1 seamless visual — you see the result, not the math.

**Keywords:** ocean wave, trend visualizer, wave chart, trading visualization, TradingView indicator, trend flow, visual trading, momentum visualization, ocean trading, wave indicator

---

## ⚡ Try It in 30 Seconds

1. **Open** the [TradingView indicator page](https://www.tradingview.com/script/4ZzTlQct-Ocean-Wave-9-Factor-Trend-Visualization/)
2. **Click** "Add to chart" (free TradingView account required)
3. **See** ocean waves — cyan = rising tide, indigo = undertow, slate = calm waters

That's it. You now see the market's flow at a glance.

---

> ### ⭐ **Star this repo** — it helps other traders discover Ocean Wave!

---

## 🌊 How It Works

### The Idea

The market isn't a bar chart — it's a flow. Ocean Wave visualizes that flow as ocean waves:

- **🌊 Rising Tide** (cyan/teal waves) = bullish trend context
- **🌀 Undertow** (indigo/violet waves) = bearish trend context
- **~ Calm Waters** (slate waves) = neutral/ranging market
- **Wave size** = trend strength (bigger waves = stronger trend)

### 9 Factors, 1 Visual

Inside Ocean Wave, 9 technical factors work together — invisibly:

| Factor | What It Measures |
|--------|-----------------|
| MA Crossover (20/50) | Base trend direction |
| Volume Confirmation | Signal strength |
| Momentum Check | Price vs MA position |
| RSI (14) | Overbought/oversold |
| ADX (14) | Trend strength |
| MACD (12/26/9) | Momentum crossover |
| ATR (14) | Volatility assessment |
| Bollinger Bands (20, 2σ) | Price position, squeeze |
| Stochastic (14/3/3) | Momentum oscillator |

You don't need to read 9 indicators. The ocean does it for you.

### Output

- **Wave color:** Cyan (bullish) / Indigo (bearish) / Slate (neutral)
- **Wave height:** Trend strength (bigger waves = stronger trend)
- **3-layer depth:** Surface + deep + floor waves for ocean depth effect
- **Minimal label:** Just "🌊 Rising Tide" or "🌀 Undertow" — no numbers
- **No tables, no factor breakdowns, no clutter**

## 🚀 Installation (TradingView)

### v3.2 — Wave Visualizer + Auto-Preset + Dynamic HTF (latest)

1. Open TradingView → Pine Editor
2. Copy the contents of `pine/ocean-wave-v3.2.pine`
3. Paste into Pine Editor
4. Click "Add to chart"
5. Preset auto-detects from chart timeframe (or choose manually: Scalping / Swing / Position)
6. Enable MTF mode to see higher timeframe trend with dynamic tint intensity

### v3.1 — Wave Visualizer + MTF + Presets

### v3.0 — Wave Visualizer (stable)

### v2.1 — Classic Zones (legacy)

The previous version with colored zones (green/yellow/red), factor tables, and confidence percentages. Available as `pine/ocean-wave-v2.1.pine` (full) and `pine/ocean-wave-lite-v2.1.pine` (lite).

## 📁 Repository Structure

```
ocean-wave-indicator/
├── README.md (this file)
├── LICENSE (Mozilla Public License 2.0)
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── pine/
│   ├── ocean-wave-v3.2.pine       # Wave Visualizer + Auto-Preset + Dynamic HTF (latest)
│   ├── ocean-wave-v3.1.pine       # Wave Visualizer + MTF + Presets
│   ├── ocean-wave-v3.0.pine       # Wave Visualizer (stable)
│   ├── ocean-wave-v2.1.pine       # Classic zones with tables (legacy)
│   ├── ocean-wave-lite-v2.1.pine  # Lite zone-only (legacy)
│   └── CHANGELOG.md
├── python/
│   ├── nonuple_algorithm.py        # Reference Python implementation
│   └── validate_pine_csv.py        # Validation script
├── backtest/
│   └── results/                    # Backtest data (JSON)
└── docs/
    ├── algorithm.md
    ├── architecture.md
    ├── backtest-results.md
    └── example-configs.md
```

## 🔔 Alerts

Ocean Wave includes ocean-themed alerts:

| Alert | Trigger |
|-------|---------|
| 🌊 Tide Rising | Bullish trend detected |
| 🌀 Undertow | Bearish trend detected |
| 🔄 Tide Shift | Trend direction changed |
| ⚡ Strong Current | High confidence trend |
| 🔥 High Energy | Strong trend (80+ strength) |
| 🌊 Wave Alignment | 4+ factors agree |
| 📊 HTF Trend Change | Higher timeframe trend shifted |
| 📊 HTF Tide Rising | Higher timeframe turning bullish |
| 📊 HTF Undertow | Higher timeframe turning bearish |

## 🎨 Customization

- **Wave Intensity** — control wave height (0.5x to 3.0x)
- **Presets** — Auto (detects from chart timeframe), Scalping (fast), Swing (default), Position (slow) — one-click setup
- **Dynamic HTF Tint** — MTF background tint intensity scales with HTF trend strength (stronger HTF = more visible)
- **Multi-Timeframe** — see higher timeframe trend as background tint + label
- **Smooth Color Transitions** — gradual color shifts between trend states
- **Ocean Colors** — fully customizable palette
- **Wave Layers** — surface, deep, and floor waves
- **MA Lines** — optional, off by default for clean visual
- **Trend Label** — minimal emoji + text, no numbers

## 📊 Backtest Results

Detailed backtest results available in [docs/backtest-results.md](docs/backtest-results.md). Ocean Wave is a **visualization tool**, not a signal service. It shows you the market's flow — it doesn't tell you when to buy or sell.

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md). Areas of interest:

- Visualization improvements (make it look even more like ocean waves)
- Additional color palettes and themes
- Multi-timeframe analysis
- Performance optimizations

## 📄 License

Mozilla Public License 2.0 — use freely, modify, share.

## 🔗 Links

- [Ocean View App](https://yaroslavmak1995-prog.github.io/ocean-view-app/) — Web dashboard
- [TradingView](https://www.tradingview.com/script/4ZzTlQct-Ocean-Wave-9-Factor-Trend-Visualization/) — Install indicator
- [Algorithm Documentation](docs/algorithm.md)
- [Backtest Results](docs/backtest-results.md)
- [Validation Results](docs/validation-results.md)

---

Built with ❤️ by the Ocean View team. Not financial advice. DYOR.

## 📋 Roadmap

- ✅ v1.0 — Initial 9-factor indicator
- ✅ v2.1 — Confidence smoothing + 11 alert conditions
- ✅ v3.0 — Wave visualizer with ocean colors, 3-layer depth, no tables
- ✅ v3.1 — Multi-timeframe mode + preset dropdowns + smooth color transitions
- ✅ v3.2 — Auto-preset detection + dynamic HTF tint + combined security calls + alert summary
- 🔵 v4.0 — Animated wave transitions + true color interpolation