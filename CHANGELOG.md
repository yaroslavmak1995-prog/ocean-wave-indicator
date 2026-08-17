# CHANGELOG — Ocean Wave Indicator

## v3.1 (2026-08-17) — Multi-Timeframe + Presets + Color Transitions

### Added
- **Multi-Timeframe (MTF) mode** — see higher timeframe trend (D1, W1) while on a lower timeframe chart. Subtle background tint + HTF label + 3 MTF alerts
- **Preset dropdown** — Scalping (fast MAs, low wave intensity), Swing (default), Position (slow MAs, high wave intensity). One-click setup for different trading styles
- **Smooth color transitions** — EMA-based transition factor gradually shifts wave colors between bullish/bearish/neutral instead of hard switching. Toggleable via input
- **3 new MTF alerts** — HTF Trend Change, HTF Tide Rising, HTF Undertow

### Changed
- MA, RSI, ADX lengths now use preset-overrideable effective values
- Wave intensity also responds to preset selection
- `max_boxes_count=50` added to indicator declaration for HTF label

### Preset Details
| Preset | MA Fast | MA Slow | RSI | ADX | Wave Intensity |
|--------|---------|---------|-----|-----|----------------|
| Default | 20 | 50 | 14 | 14 | 1.5x |
| Scalping | 9 | 21 | 7 | 10 | 1.0x |
| Swing | 20 | 50 | 14 | 14 | 1.5x |
| Position | 50 | 200 | 21 | 20 | 2.5x |

### Addresses GitHub Issues
- Closes #2 (Multi-timeframe mode)
- Closes #10 (Usage examples for different trading styles — via presets)

## v3.0 (2026-08-16) — Wave Visualizer 🌊

### Complete Repackage: Indicator → Visualizer

This is not an incremental update. v3.0 is a complete reimagining of Ocean Wave — from a technical indicator with tables and numbers to a visual trend flow tool with ocean waves.

### Added
- **3-layer wave visualization** — surface, deep, and floor wave fills using `plot()` + `fill()`, creating an ocean depth effect
- **Ocean color palette** — cyan/teal (bullish), indigo/violet (bearish), slate (neutral). No more generic green/red
- **Wave height proportional to trend strength** — bigger waves = stronger trend (visual encoding)
- **EMA-smoothed wave boundaries** — organic, flowing curves instead of jagged lines
- **Wave Intensity input** — customizable wave height multiplier (0.5x to 3.0x)
- **Minimal trend label** — just "🌊 Rising Tide" / "🌀 Undertow" / "~ Calm Waters" — no numbers
- **Ocean-themed alerts** — "Tide Rising", "Undertow", "Tide Shift", "Strong Current", "Wave Alignment"
- **Clean, minimal design** — think music visualizer, not Bloomberg Terminal

### Removed
- ❌ Factor table (9 rows with individual factor data) — contradicts "visual" promise
- ❌ Confidence table (bottom-right) — no numbers on the visual
- ❌ Signal label with percentages — too technical
- ❌ bgcolor green/yellow/red zones — "банально", every indicator has this
- ❌ "45% win rate (below random 50%)" in header — anti-advertising
- ❌ "THIS IS A VISUALIZATION TOOL, NOT A SIGNAL SERVICE" in header — too defensive
- ❌ All backtest references in user-facing code — moved to GitHub docs only
- ❌ MA lines on by default — off for clean visual

### Preserved (invisible to user)
- ✅ 9-factor algorithm (MA, Volume, RSI, ADX, MACD, ATR, BB, Stochastic, Synergy)
- ✅ Zone calculation (bullish/bearish/neutral)
- ✅ Confidence calculation (internal only, not displayed)
- ✅ All alert conditions (with improved copy)

### Impact
- Completely different visual identity — no other TradingView indicator looks like this
- Removed all anti-advertising from user-facing code
- TradingView SEO optimized for "Ocean Wave" search
- Fresh start for marketing and community perception

## v2.1 (2026-08-05) — Confidence Smoothing + Zone Change Alerts

### Added
- **Confidence Smoothing (EMA-based)** — configurable length (default: 3 bars), toggleable. Addresses Issue #3 (GOOGL 0%→87% in 1 day).
- **Rate-limiting for confidence changes** — max confidence change per bar (default: 20pp). Prevents wild swings.
- **Zone change alerts** — 3 new alert conditions: `zone_to_red` (green/yellow → red), `zone_to_green` (red/yellow → green), `zone_changed` (any zone change). Addresses Issue #1.
- **Confidence threshold alerts** — 2 new alert conditions: confidence crosses above/below configurable threshold (default: 50). Addresses Issue #2.
- **Total alert conditions: 6 → 11** (6 original + 5 new)

### New Inputs
- `use_confidence_smoothing` (bool, default: true)
- `confidence_ema_len` (int, default: 3, range: 1-10)
- `max_conf_change` (int, default: 20, range: 5-50)
- `conf_thresh` (int, default: 50, range: 10-90)

### Impact
- Confidence scores are now smoother and more stable
- Traders can set alerts for zone changes without watching the chart
- Backward compatible — smoothing can be disabled to get v1.1 behavior

## v1.1 (2026-07-26) — Confidence Fix & Algorithm Alignment

### Fixed
- **CONFIDENCE DOUBLE-COUNTING BUG** — RSI, ADX, MACD, ATR, BB, Stochastic bonuses were applied both in `total_strength` AND again in `confidence` adjustments (v1.0). Now each bonus is counted EXACTLY ONCE. Confidence = total_strength + synergy_bonus only.
- **Lite ≠ Full algorithm** — Lite v1.0 used majority-vote (different from Full). Lite v1.1 now uses the EXACT SAME algorithm as Full v1.1, just without tables.
- **Signal label simplified** — was `"Strong Uptrend ↑\n65% conf | 58% str"`, now `"Strong Uptrend\n65% conf"` (cleaner, confidence is the primary metric)

### Impact
- Confidence scores will be LOWER and more honest (~20-30pp reduction)
- Lite and Full will produce IDENTICAL zone colors on the same chart
- Signal label is shorter and clearer
- Backtest results may change (lower confidence = different high/low conf split)

## v1.0 (2026-07-24) — Initial Release

### Added
- Full 9-factor indicator (MA, Volume, Momentum, RSI, ADX, MACD, ATR, BB, Stochastic)
- Zone background coloring (5 levels: green/light_green/yellow/light_red/red)
- Factor table (9 factors with emoji + values)
- Confidence table (confidence, strength, confirmations, synergy)
- Signal label (trend direction + confidence %)
- 5 alert conditions (Uptrend Start, Downtrend Start, Neutral Start, High Confidence, High Strength)
- Configurable inputs for all indicator periods and thresholds
- MA Fast/Slow lines + Bollinger Bands overlay
- Lite version (zones + MAs + signal label only)

### Known Issues
- ⚠️ **Confidence double-counting**: RSI, ADX, MACD, ATR, BB, Stochastic bonuses are applied both in `total_strength` calculation AND again in `confidence` adjustments. This inflates confidence scores by ~20-30pp. Fix planned for v1.1.
- ⚠️ **Lite ≠ Full algorithm**: Lite version uses majority-vote (8 factors, ≥3 = uptrend), Full uses bonus accumulation. They produce different zone colors on the same chart. Fix planned for v1.1 (Lite should use same algorithm, just without tables).
- ⚠️ **Signal label text**: Too long ("Strong Uptrend ↑\n65% conf | 58% str"). Simplify in v1.1.

### Backtest Results (v1.0)
- 5-year × 5 ticker: 45.32% average win rate (below random)
- High confidence accuracy: 47.48% (not significantly better than low: 42.64%)
- Validation vs Python: 100% trend direction match, 60.7% zone match, 26.6pp strength diff