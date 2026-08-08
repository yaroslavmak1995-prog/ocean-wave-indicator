# Ocean Wave — Example Configurations

Different trading styles need different settings. Here are sample configurations for common trading styles.

## All Configurations

| Parameter | Scalping | Swing Trading | Position Trading |
|-----------|----------|---------------|------------------|
| `ma_fast` | 9 | 20 | 50 |
| `ma_slow` | 21 | 50 | 200 |
| `rsi_len` | 7 | 14 | 21 |
| `rsi_ob` | 75 | 70 | 65 |
| `rsi_os` | 25 | 30 | 35 |
| `adx_len` | 10 | 14 | 20 |
| `adx_thresh` | 20 | 25 | 30 |
| `macd_fast` | 5 | 12 | 26 |
| `macd_slow` | 13 | 26 | 52 |
| `macd_signal` | 4 | 9 | 18 |
| `atr_len` | 10 | 14 | 20 |
| `bb_len` | 15 | 20 | 30 |
| `bb_mult` | 2.0 | 2.0 | 2.5 |
| `stoch_len` | 9 | 14 | 21 |
| `stoch_smooth` | 3 | 3 | 5 |
| `use_confidence_smoothing` | true | true | true |
| `confidence_ema_len` | 2 | 3 | 5 |
| `max_conf_change` | 25 | 20 | 15 |
| `conf_thresh` | 60 | 50 | 40 |

## Scalping (1m–15m charts)

**Goal:** Fast signals for quick entries/exits. More sensitive to short-term momentum.

**Key differences:**
- Shorter MA periods (9/21) — react faster to price changes
- Tighter RSI bands (25/75) — only extreme readings trigger signals
- Shorter ADX (10) — picks up brief momentum bursts
- Higher confidence threshold (60) — only high-conviction setups
- Higher max confidence change (25) — allow faster confidence shifts

**Best for:** Crypto futures, forex majors, high-liquid stocks during market hours.

## Swing Trading (1H–4H charts)

**Goal:** Capture multi-day moves. Balanced between sensitivity and reliability.

**Key differences:**
- Standard MA periods (20/50) — the classic trend-following setup
- Standard RSI bands (30/70) — conventional overbought/oversold
- Standard ADX (14, threshold 25) — moderate trend strength filter
- Medium confidence threshold (50) — balanced entry filter
- Medium confidence smoothing (3 bars) — smooth but responsive

**Best for:** Stocks, index ETFs, forex during active sessions.

## Position Trading (Daily–Weekly charts)

**Goal:** Identify long-term trends. Slow, deliberate signals.

**Key differences:**
- Long MA periods (50/200) — golden cross / death cross territory
- Wider RSI bands (35/65) — only major momentum shifts matter
- Longer ADX (20, threshold 30) — only strong, sustained trends
- Lower confidence threshold (40) — accept lower conviction on long timeframes
- Stronger smoothing (5 bars, max change 15) — very smooth confidence

**Best for:** IRA/401k allocation, long-term crypto holdings, macro trend identification.

## How to Apply

1. Open TradingView → Pine Editor
2. Load Ocean Wave (Full or Lite v2.1)
3. Click the gear icon ⚙️ on the indicator
4. Adjust parameters to match your trading style
5. Click OK

## Tips

- **Start with the Swing Trading preset** — it's the most balanced
- **Scalping preset will produce more signals** but with lower accuracy
- **Position Trading preset will produce fewer signals** but with higher reliability
- **Confidence smoothing helps all styles** — keep it enabled
- **Adjust `max_conf_change` based on your timeframe** — shorter timeframe = higher value

## Backtest Disclaimer

These configurations have NOT been individually backtested. The 45.32% win rate is from the default (Swing Trading) configuration. Your results may vary. Always backtest before using real money.

---

Built with ❤️ by the Ocean View team. Not financial advice. DYOR.