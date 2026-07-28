# Ocean Wave Algorithm — Detailed Description

## Overview

Ocean Wave is a **9-factor trend visualization** algorithm that fuses 9 technical indicators into a single colored zone signal. It is NOT a trading signal service — the 5-year backtest shows 45.32% win rate (below random).

## Algorithm Flow

```
Price Data (OHLCV)
       ↓
9 Indicator Calculations
       ↓
Factor Bonus Accumulation (-15 to +15 each)
       ↓
Total Strength Calculation (0-100)
       ↓
Confirmation Count (0-6) + Confidence Floor
       ↓
Synergy Bonus (+10 if 4+ agree)
       ↓
Confidence Calculation (0-100%)
       ↓
Zone Color (5 levels)
       ↓
Visualization (zones, tables, labels, alerts)
```

## Factor Calculations

### 1. MA Crossover (20/50)

- **MA Fast** = SMA(close, 20)
- **MA Slow** = SMA(close, 50)
- **Diff%** = (MA Fast - MA Slow) / MA Slow × 100
- **Base Trend** = +1 if diff > 0.5%, -1 if diff < -0.5%, else 0
- **Base Strength** = |diff%| × 15

### 2. Volume Confirmation

- **Volume Ratio** = volume / SMA(volume, 20)
- **Bonus**: +15 (ratio > 2.0), +10 (> 1.5), +5 (> 1.2), -5 (< 0.8), -10 (< 0.5)

### 3. Momentum Check

- **Momentum%** = (close - MA Fast) / MA Fast × 100
- **Bonus**: +10 (|m| > 3%), +5 (|m| > 1.5%), -5 (|m| < 0.5%)

### 4. RSI (14)

- Standard RSI calculation with configurable overbought/oversold thresholds
- **Bonus**: -10 to +15 depending on trend alignment and overbought/oversold

### 5. ADX (14)

- DMI+ and DMI- direction detection
- **Bonus**: -15 (weak trend) to +15 (strong trend in direction)

### 6. MACD (12/26/9)

- Standard MACD with signal line crossover detection
- **Bonus**: -10 to +15 depending on trend alignment

### 7. ATR (14)

- ATR as percentage of price
- **Bonus**: -15 (extreme volatility) to +3 (low volatility)

### 8. Bollinger Bands (20, 2σ)

- %B position, bandwidth, squeeze detection
- **Bonus**: -16 to +7 depending on position and squeeze

### 9. Stochastic Oscillator (14/3/3)

- %K and %D with crossover detection
- **Bonus**: -7 to +8 depending on overbought/oversold and trend alignment

## Aggregation

### Total Strength
```
total_strength = base_strength + volume_bonus + momentum_bonus + rsi_bonus + adx_bonus + macd_bonus + atr_bonus + bb_bonus + stoch_bonus
total_strength = clamp(0, 100, total_strength)
```

### Confirmation Count
Count of factors with non-negative bonus (0-6 factors).

### Confidence Floor
- If 3+ confirmations and trend ≠ neutral: strength += 10
- If 5+ confirmations and trend ≠ neutral: strength += 15

### Synergy Bonus
If 4+ out of 6 indicators agree with trend direction: confidence += 10

### Confidence (v1.0 — HAS DOUBLE-COUNTING BUG)
⚠️ In v1.0, confidence is calculated as `total_strength` PLUS additional adjustments for each indicator AGAIN. This means RSI, ADX, MACD, ATR, BB, and Stochastic bonuses are counted 2-3 times.

**v1.1 will fix this** by using: `confidence = total_strength + synergy_bonus`, without re-adding indicator bonuses.

## Zone Colors

| Zone | Condition | Meaning |
|------|-----------|---------|
| Strong Green | trend=uptrend, strength≥70 | Strong uptrend context |
| Light Green | trend=uptrend, strength<70 | Moderate uptrend context |
| Yellow | trend=neutral | Consolidation / ranging |
| Light Red | trend=downtrend, strength<70 | Moderate downtrend context |
| Strong Red | trend=downtrend, strength≥70 | Strong downtrend context |

## Backtest Results

See [backtest-results.md](backtest-results.md) for full data.

**Summary**: 45.32% average win rate across 5 tickers over 5 years. Below random (50%). This confirms: **visualization tool, not signal service**.