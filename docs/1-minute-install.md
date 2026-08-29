# ⚡ 1-Minute Install Guide

## Option A: TradingView (30 seconds)

1. Open [TradingView](https://www.tradingview.com/) → any chart
2. Open **Pine Editor** (bottom panel)
3. Copy the contents of [`pine/ocean-wave-v3.2.pine`](../pine/ocean-wave-v3.2.pine)
4. Paste into Pine Editor → click **"Add to chart"**
5. Done! 🌊 You should see ocean waves on your chart.

> **No Pro account needed.** Free TradingView accounts can use community scripts.

---

## Option B: HTML Demo (10 seconds, no account)

Once GitHub Pages is enabled:

1. Open `https://yaroslavmak1995-prog.github.io/ocean-wave-indicator/`
2. See animated ocean waves immediately — no signup, no install
3. Click "📋 Copy Pine Script" to get the code for TradingView

---

## After Install — What You'll See

| Visual | Meaning |
|--------|---------|
| 🌊 Cyan waves | Bullish trend (rising tide) |
| 🌀 Indigo waves | Bearish trend (undertow) |
| ~ Slate waves | Neutral / ranging market |
| Big waves | Strong trend |
| Small waves | Weak trend |
| 9-Factor Table | Shows which of 9 factors are bullish/bearish/neutral |

## First Steps

1. **Try different tickers** — the waves adapt automatically
2. **Switch timeframes** — auto-preset detects and adjusts (Scalping < 15m, Swing 15m-4h, Position > 4h)
3. **Enable MTF mode** — see higher timeframe trend as background tint
4. **Set alerts** — 11 ocean-themed alerts (🌊 Tide Rising, 🌀 Undertow, etc.)
5. **Disable table** — for pure wave visual, uncheck "Show Factor Table" in settings

## Common Questions

**Q: Does this tell me when to buy/sell?**
A: No. Ocean Wave is a **visualization tool** — it shows you the market's flow at a glance. It helps you understand the trend context, but entry/exit decisions are yours.

**Q: How is this different from using 9 separate indicators?**
A: You'd need 9 indicator panels cluttering your screen, and you'd have to mentally synthesize them. Ocean Wave does the synthesis visually — one wave, one glance.

**Q: Is the backtest good?**
A: Honest answer: 45% win rate as a directional signal. Ocean Wave is better for *understanding* the market than *predicting* it. See [backtest results](backtest-results.md).

**Q: Can I modify it?**
A: Yes! MPL 2.0 license — fork it, modify it, share your improvements. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Need Help?

- [GitHub Discussions](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions) — ask anything
- [Issue Tracker](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues) — report bugs
- [Full README](../README.md) — complete documentation