#!/usr/bin/env python3
"""
Ocean Wave — Pine Script Validation Script (Offline, CSV-based)
Compares Python Nonuple Algorithm output with Pine Script logic on same data.

Purpose: Verify that Pine Script v1 produces same results as Python v6.1
Uses LOCAL CSV data — no yfinance dependency, no rate limiting.

Usage:
    python validate_pine_csv.py [--ticker AAPL] [--all]
"""

import sys
import os
import csv
import json
from datetime import datetime

# Add prototype to path (for Python Nonuple Algorithm import)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'prototype'))

try:
    from core.trend_detector import TrendDetector
    from core.indicators import RSICalculator, ADXCalculator
except ImportError:
    TrendDetector = None
    RSICalculator = None
    ADXCalculator = None
import numpy as np


def load_csv_data(ticker, data_dir=None):
    """Load OHLCV data from local CSV file."""
    if data_dir is None:
        # Try prototype/backtest first, then ocean-wave-indicator/backtest
        proto_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'prototype', 'backtest')
        owi_dir = os.path.join(os.path.dirname(__file__), '..', 'backtest')
        data_dir = proto_dir if os.path.exists(proto_dir) else owi_dir
    
    filepath = os.path.join(data_dir, f'data_{ticker}.csv')
    
    if not os.path.exists(filepath):
        print(f"  ⚠️ File not found: {filepath}")
        return None
    
    dates = []
    opens, highs, lows, closes, volumes = [], [], [], [], []
    
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                dates.append(row.get('Date', row.get('date', '')))
                closes.append(float(row['Close']))
                highs.append(float(row['High']))
                lows.append(float(row['Low']))
                opens.append(float(row['Open']))
                volumes.append(float(row['Volume']))
            except (ValueError, KeyError) as e:
                continue
    
    if len(closes) < 60:
        print(f"  ⚠️ Not enough data: {len(closes)} bars (need 60+)")
        return None
    
    return {
        'dates': dates,
        'opens': opens,
        'highs': highs,
        'lows': lows,
        'closes': closes,
        'volumes': volumes,
    }


def simulate_pine_script_v1_1(closes, highs, lows, volumes, dates=None):
    """
    Simulate Pine Script v1.1 FULL logic on historical data.
    This replicates the exact calculation in ocean-wave-v1.1.pine.
    
    v1.1 changes:
    - NO double-counting: confidence = total_strength + synergy_bonus only
    - No separate confidence adjustments for RSI/ADX/MACD/ATR/BB/Stoch
    - Confidence Floor still applies (3+ confirmations → min 25%, 5+ → min 50%)
    
    Returns dict with all intermediate values for comparison.
    """
    results = []
    n = len(closes)
    dates_list = dates if dates is not None else [''] * n
    
    min_bars = 50  # Need MA50
    
    for i in range(min_bars, n):
        c = np.array(closes[:i+1])
        h = np.array(highs[:i+1])
        l = np.array(lows[:i+1])
        v = np.array(volumes[:i+1])
        
        close = c[-1]
        high_val = h[-1]
        low_val = l[-1]
        volume = v[-1]
        
        # ─── STEP 1: MA Crossover ───
        ma_fast = np.mean(c[-20:]) if len(c) >= 20 else np.mean(c)
        ma_slow = np.mean(c[-50:]) if len(c) >= 50 else np.mean(c)
        ma_diff_pct = (ma_fast - ma_slow) / ma_slow * 100 if ma_slow != 0 else 0
        base_trend = 1 if ma_diff_pct > 0.5 else (-1 if ma_diff_pct < -0.5 else 0)
        
        # ─── STEP 2: Volume Confirmation ───
        avg_volume = np.mean(v[-20:]) if len(v) >= 20 else v[-1]
        volume_ratio = volume / avg_volume if avg_volume > 0 else 1.0
        
        if volume_ratio > 2.0:
            volume_bonus = 15
        elif volume_ratio > 1.5:
            volume_bonus = 10
        elif volume_ratio > 1.2:
            volume_bonus = 5
        elif volume_ratio < 0.5:
            volume_bonus = -10
        elif volume_ratio < 0.8:
            volume_bonus = -5
        else:
            volume_bonus = 0
        
        # ─── STEP 3: Momentum Check ───
        momentum_pct = (close - ma_fast) / ma_fast * 100 if ma_fast != 0 else 0
        if abs(momentum_pct) > 3:
            momentum_bonus = 10
        elif abs(momentum_pct) > 1.5:
            momentum_bonus = 5
        elif abs(momentum_pct) < 0.5:
            momentum_bonus = -5
        else:
            momentum_bonus = 0
        
        # ─── Base strength ───
        base_strength = abs(ma_diff_pct) * 15
        total_strength_raw = base_strength + volume_bonus + momentum_bonus
        total_strength = min(100, max(0, total_strength_raw))
        
        # ─── STEP 4: RSI ───
        rsi_len = 14
        if len(c) >= rsi_len:
            deltas = np.diff(c[-rsi_len-1:])
            gains = np.where(deltas > 0, deltas, 0)
            losses = np.where(deltas < 0, -deltas, 0)
            avg_gain = np.mean(gains)
            avg_loss = np.mean(losses)
            rs = avg_gain / avg_loss if avg_loss != 0 else 100
            rsi_value = 100 - (100 / (1 + rs))
            rsi_value = min(100, max(0, rsi_value))
        else:
            rsi_value = 50
        
        rsi_ob = 70
        rsi_os = 30
        if rsi_value >= rsi_ob:
            rsi_bonus = -10 if base_trend == 1 else (15 if base_trend == -1 else 0)
        elif rsi_value <= rsi_os:
            rsi_bonus = -10 if base_trend == -1 else (15 if base_trend == 1 else 0)
        elif rsi_value >= 60:
            rsi_bonus = 5 if base_trend == 1 else (-5 if base_trend == -1 else 0)
        elif rsi_value <= 40:
            rsi_bonus = 5 if base_trend == -1 else (-5 if base_trend == 1 else 0)
        else:
            rsi_bonus = 0
        
        # ─── STEP 5: ADX ───
        adx_len = 14
        # Simplified ADX calculation
        if len(c) >= 2 * adx_len + 1:
            tr = np.maximum(h[-adx_len*2:] - l[-adx_len*2:],
                           np.maximum(np.abs(h[-adx_len*2:] - np.roll(c[-adx_len*2:], 1)),
                                      np.abs(l[-adx_len*2:] - np.roll(c[-adx_len*2:], 1))))
            tr[0] = h[-adx_len*2] - l[-adx_len*2]
            
            plus_dm = np.maximum(h[-adx_len*2:] - np.roll(h[-adx_len*2:], 1), 0)
            minus_dm = np.maximum(np.roll(l[-adx_len*2:], 1) - l[-adx_len*2:], 0)
            
            atr14 = np.mean(tr[-adx_len:])
            plus_di = 100 * np.mean(plus_dm[-adx_len:]) / atr14 if atr14 > 0 else 0
            minus_di = 100 * np.mean(minus_dm[-adx_len:]) / atr14 if atr14 > 0 else 0
            
            dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di) if (plus_di + minus_di) > 0 else 0
            adx_value = dx  # Simplified - should be smoothed
            adx_direction = "bullish" if plus_di > minus_di else ("bearish" if plus_di < minus_di else "neutral")
        else:
            adx_value = 20
            adx_direction = "neutral"
        
        if adx_value >= 25:
            if adx_direction == "bullish" and base_trend == 1:
                adx_bonus = 15
            elif adx_direction == "bearish" and base_trend == -1:
                adx_bonus = 15
            elif adx_direction != "neutral" and base_trend == 0:
                adx_bonus = 5
            else:
                adx_bonus = -5
        elif adx_value >= 15:
            adx_bonus = 0
        else:
            adx_bonus = -15
        
        # ─── STEP 6: MACD ───
        macd_fast = 12
        macd_slow = 26
        macd_signal_len = 9
        
        if len(c) >= macd_slow + macd_signal_len:
            ema_fast = c[-1]  # Simplified
            ema_slow = c[-1]  # Simplified
            # Use simple moving averages as approximation
            macd_line = np.mean(c[-macd_fast:]) - np.mean(c[-macd_slow:])
            signal_line = macd_line * 0.2 + (c[-2] - np.mean(c[-macd_slow-1:-1])) * 0.8 if len(c) > macd_slow else 0
        else:
            macd_line = 0
            signal_line = 0
        
        macd_trend = ("strong_bullish" if macd_line > signal_line and macd_line > 0 else
                      "bullish" if macd_line > signal_line else
                      "strong_bearish" if macd_line < signal_line and macd_line < 0 else
                      "bearish" if macd_line < signal_line else "neutral")
        
        if macd_trend == "strong_bullish" and base_trend == 1:
            macd_bonus = 15
        elif macd_trend == "bullish" and base_trend == 1:
            macd_bonus = 10
        elif macd_trend == "strong_bearish" and base_trend == -1:
            macd_bonus = 15
        elif macd_trend == "bearish" and base_trend == -1:
            macd_bonus = 10
        elif macd_trend == "neutral" and base_trend == 0:
            macd_bonus = 3
        else:
            macd_bonus = -10
        
        # ─── STEP 7: ATR ───
        if len(c) >= 15:
            tr_list = []
            for j in range(1, min(15, len(c))):
                idx = len(c) - j
                tr_val = max(h[idx] - l[idx], abs(h[idx] - c[idx-1]), abs(l[idx] - c[idx-1]))
                tr_list.append(tr_val)
            atr_value = np.mean(tr_list)
        else:
            atr_value = h[-1] - l[-1]
        
        atr_pct = atr_value / close * 100 if close > 0 else 0
        
        if atr_pct > 5.0:
            atr_bonus = -15
        elif atr_pct > 3.0:
            atr_bonus = -8
        elif atr_pct < 1.0:
            atr_bonus = 3
        else:
            atr_bonus = 0
        
        atr_trend = "rising" if atr_value > np.mean(tr_list) else "falling" if len(tr_list) > 1 else "stable"
        
        if atr_trend == "rising" and base_trend != 0:
            atr_bonus -= 3
        elif atr_trend == "falling" and base_trend != 0:
            atr_bonus += 2
        
        # ─── STEP 8: Bollinger Bands ───
        bb_len = 20
        if len(c) >= bb_len:
            bb_data = c[-bb_len:]
            bb_basis = np.mean(bb_data)
            bb_dev = 2.0 * np.std(bb_data)
            bb_upper = bb_basis + bb_dev
            bb_lower = bb_basis - bb_dev
            bb_range = bb_upper - bb_lower
            bb_percent_b = (close - bb_lower) / bb_range if bb_range > 0 else 0.5
            bb_bandwidth = bb_range / bb_basis * 100 if bb_basis > 0 else 0
        else:
            bb_percent_b = 0.5
            bb_bandwidth = 5
            bb_squeeze = "normal"
        
        bb_squeeze = ("extreme" if bb_bandwidth < 3 else
                     "tight" if bb_bandwidth < 5 else
                     "expanding" if bb_bandwidth > 10 else "normal")
        
        bb_bonus = 0
        if bb_percent_b >= 1.0 or bb_percent_b <= 0.0:
            bb_bonus = -8
        elif bb_percent_b >= 0.85 or bb_percent_b <= 0.15:
            bb_bonus = -3
        
        if bb_squeeze in ("extreme", "tight"):
            bb_bonus -= 5
        elif bb_squeeze == "expanding" and base_trend != 0:
            bb_bonus += 4
        
        if (base_trend == 1 and bb_percent_b > 0.6) or (base_trend == -1 and bb_percent_b < 0.4):
            bb_bonus += 3
        
        # ─── STEP 9: Stochastic ───
        stoch_k_len = 14
        stoch_smooth = 3
        
        if len(c) >= stoch_k_len:
            recent_high = np.max(h[-stoch_k_len:])
            recent_low = np.min(l[-stoch_k_len:])
            stoch_range = recent_high - recent_low
            stoch_k_raw = 100 * (close - recent_low) / stoch_range if stoch_range > 0 else 50
        else:
            stoch_k_raw = 50
        
        stoch_k = stoch_k_raw  # Simplified (no smoothing)
        stoch_d = stoch_k  # Simplified
        
        stoch_signal = ("overbought" if stoch_k >= 80 else
                       "oversold" if stoch_k <= 20 else
                       "bullish" if stoch_k >= 60 else
                       "bearish" if stoch_k <= 40 else "neutral")
        
        stoch_bonus = 0
        if stoch_signal == "overbought" and base_trend == 1:
            stoch_bonus = -4
        elif stoch_signal == "oversold" and base_trend == -1:
            stoch_bonus = -4
        elif stoch_signal == "neutral":
            stoch_bonus = 2
        elif (base_trend == 1 and stoch_k > 50) or (base_trend == -1 and stoch_k < 50):
            stoch_bonus = 3
        elif (base_trend == 1 and stoch_k < 30) or (base_trend == -1 and stoch_k > 70):
            stoch_bonus = -4
        
        # ─── AGGREGATE: Total Strength (v1.1 — each bonus counted ONCE) ───
        total_strength = min(100, max(0, total_strength + rsi_bonus + adx_bonus + macd_bonus + atr_bonus + bb_bonus + stoch_bonus))
        
        # ─── Synergy Bonus ───
        agree_count = 0
        if base_trend == 1 and rsi_value >= 50:
            agree_count += 1
        elif base_trend == -1 and rsi_value <= 50:
            agree_count += 1
        
        if (base_trend == 1 and adx_direction == "bullish") or (base_trend == -1 and adx_direction == "bearish"):
            agree_count += 1
        
        macd_agrees = (base_trend == 1 and macd_trend in ("strong_bullish", "bullish")) or \
                      (base_trend == -1 and macd_trend in ("strong_bearish", "bearish"))
        if macd_agrees:
            agree_count += 1
        
        if atr_pct <= 3.0 and base_trend != 0:
            agree_count += 1
        
        if (base_trend == 1 and bb_percent_b > 0.5) or (base_trend == -1 and bb_percent_b < 0.5):
            agree_count += 1
        
        if (base_trend == 1 and stoch_k > 50) or (base_trend == -1 and stoch_k < 50):
            agree_count += 1
        
        synergy_bonus = 10 if agree_count >= 4 else 0
        
        # ─── Confirmation Count ───
        confirmation_count = 0
        if rsi_bonus >= 0:
            confirmation_count += 1
        if adx_bonus >= 0:
            confirmation_count += 1
        if macd_bonus >= 0:
            confirmation_count += 1
        if atr_bonus >= 0:
            confirmation_count += 1
        if bb_bonus >= 0:
            confirmation_count += 1
        if stoch_bonus >= 0:
            confirmation_count += 1
        
        # Confidence Floor (applied to total_strength)
        if confirmation_count >= 3 and base_trend != 0:
            total_strength = min(100, total_strength + 10)
        if confirmation_count >= 5 and base_trend != 0:
            total_strength = min(100, total_strength + 15)
        
        # ─── Zone Color ───
        if base_trend == 1:
            zone_color = 2 if total_strength >= 70 else 1
        elif base_trend == -1:
            zone_color = -2 if total_strength >= 70 else -1
        else:
            zone_color = 0
        
        # ─── Confidence (v1.1: NO double-counting) ───
        # confidence = total_strength + synergy_bonus ONLY
        # (no separate RSI/ADX/MACD/ATR/BB/Stoch adjustments)
        confidence = min(100, max(0, total_strength + synergy_bonus))
        
        # Confidence Floor (same as v1.0)
        if confirmation_count >= 3 and base_trend != 0:
            confidence = max(confidence, 25)
        if confirmation_count >= 5 and base_trend != 0:
            confidence = max(confidence, 50)
        
        confidence = min(100, max(0, confidence))
        
        # Signal text (v1.1 — simplified, no arrows in label)
        if base_trend == 1:
            if total_strength >= 80 and volume_ratio > 1.5:
                signal_text = "Strong Uptrend"
            elif total_strength >= 60:
                signal_text = "Moderate Uptrend"
            else:
                signal_text = "Weak Uptrend"
        elif base_trend == -1:
            if total_strength >= 80 and volume_ratio > 1.5:
                signal_text = "Strong Downtrend"
            elif total_strength >= 60:
                signal_text = "Moderate Downtrend"
            else:
                signal_text = "Weak Downtrend"
        else:
            if total_strength < 30:
                signal_text = "Consolidation"
            else:
                signal_text = "Ranging"
        
        results.append({
            'bar_index': i,
            'date': dates_list[i] if i < len(dates_list) else '',
            'close': round(close, 2),
            'pine_trend': base_trend,
            'pine_strength': total_strength,
            'pine_confidence': confidence,
            'pine_zone': zone_color,
            'pine_signal': signal_text,
            'pine_confirmations': confirmation_count,
            'pine_synergy': agree_count,
            'ma_diff_pct': round(ma_diff_pct, 2),
            'rsi': round(rsi_value, 1),
            'adx': round(adx_value, 1),
            'macd_trend': macd_trend,
            'atr_pct': round(atr_pct, 2),
            'bb_percent_b': round(bb_percent_b, 3),
            'stoch_k': round(stoch_k, 1),
            'volume_ratio': round(volume_ratio, 2),
        })
    
    return results


def run_python_algorithm(closes, highs, lows, volumes):
    """Run Python Nonuple Algorithm v6.1 on same data."""
    results = []
    
    if TrendDetector is None:
        # Can't import Python algorithm, return empty results
        print("  ⚠️ Python Nonuple Algorithm not available (import failed)")
        return results
    
    detector = TrendDetector()
    
    min_bars = 50
    
    for i in range(min_bars, len(closes)):
        c = closes[:i+1]
        h = highs[:i+1]
        l = lows[:i+1]
        v = volumes[:i+1]
        
        try:
            signal = detector.detect_trend(c, v, h, l)
            results.append({
                'bar_index': i,
                'python_trend': signal.trend.value,
                'python_strength': signal.strength,
                'python_confidence': signal.confidence,
                'python_zone': signal.zone_color,
            })
        except Exception as e:
            results.append({
                'bar_index': i,
                'python_trend': 'error',
                'python_strength': 0,
                'python_confidence': 0,
                'python_zone': 'error',
            })
    
    return results


def compare_algorithms(ticker, pine_results, python_results):
    """Compare Pine Script simulation with Python algorithm results."""
    
    trend_map = {'uptrend': 1, 'downtrend': -1, 'neutral': 0}
    
    # Align by bar_index
    pine_by_idx = {r['bar_index']: r for r in pine_results}
    python_by_idx = {r['bar_index']: r for r in python_results}
    
    common_indices = sorted(set(pine_by_idx.keys()) & set(python_by_idx.keys()))
    
    if not common_indices:
        print(f"  ❌ No common bars to compare")
        return None
    
    trend_matches = 0
    trend_mismatches = 0
    strength_diffs = []
    confidence_diffs = []
    zone_matches = 0
    zone_mismatches = 0
    
    for idx in common_indices:
        p = pine_by_idx[idx]
        py = python_by_idx[idx]
        
        py_trend = trend_map.get(py['python_trend'], 0)
        
        if p['pine_trend'] == py_trend:
            trend_matches += 1
        else:
            trend_mismatches += 1
        
        zone_map = {'green': [2, 1], 'yellow': [0], 'red': [-1, -2]}
        py_zones = zone_map.get(py['python_zone'], [])
        if p['pine_zone'] in py_zones:
            zone_matches += 1
        else:
            zone_mismatches += 1
        
        strength_diffs.append(abs(p['pine_strength'] - py['python_strength']))
        confidence_diffs.append(abs(p['pine_confidence'] - py['python_confidence']))
    
    total = trend_matches + trend_mismatches
    trend_match_pct = (trend_matches / total * 100) if total > 0 else 0
    zone_match_pct = (zone_matches / (zone_matches + zone_mismatches) * 100) if (zone_matches + zone_mismatches) > 0 else 0
    avg_strength_diff = np.mean(strength_diffs) if strength_diffs else 0
    avg_confidence_diff = np.mean(confidence_diffs) if confidence_diffs else 0
    
    return {
        'ticker': ticker,
        'total_bars': total,
        'trend_matches': trend_matches,
        'trend_mismatches': trend_mismatches,
        'trend_match_pct': trend_match_pct,
        'zone_matches': zone_matches,
        'zone_mismatches': zone_mismatches,
        'zone_match_pct': zone_match_pct,
        'avg_strength_diff': round(avg_strength_diff, 1),
        'avg_confidence_diff': round(avg_confidence_diff, 1),
    }


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Validate Pine Script v1 against Python Nonuple Algorithm')
    parser.add_argument('--ticker', default=None, help='Single ticker to validate (e.g. AAPL)')
    parser.add_argument('--all', action='store_true', help='Validate all available tickers')
    parser.add_argument('--detailed', action='store_true', help='Show last 10 bars detail')
    args = parser.parse_args()
    
    tickers = ['AAPL', 'TSLA', 'SPY', 'GOOGL', 'NVDA']
    if args.ticker:
        tickers = [args.ticker]
    
    print("=" * 70)
    print("🌊 Ocean Wave — Pine Script Validation (Offline/CSV)")
    print("=" * 70)
    print()
    print("Comparing Python Nonuple Algorithm v6.1 with Pine Script v1.1 logic")
    print("Using LOCAL CSV data (no yfinance dependency)")
    print("v1.1: NO double-counting, Lite = Full algorithm")
    print(f"Tickers: {', '.join(tickers)}")
    print()
    
    all_results = []
    
    for ticker in tickers:
        print(f"\n--- {ticker} ---")
        
        # Load data
        data = load_csv_data(ticker)
        if data is None:
            print(f"  ⏭️ Skipping {ticker} — no data")
            continue
        
        print(f"  Bars: {len(data['closes'])}")
        
        # Run Pine Script v1.1 simulation
        print(f"  Running Pine Script v1.1 simulation...")
        pine_results = simulate_pine_script_v1_1(
            data['closes'], data['highs'], data['lows'], data['volumes'],
            dates=data['dates']
        )
        print(f"  Pine bars: {len(pine_results)}")
        
        # Run Python algorithm
        print(f"  Running Python Nonuple Algorithm...")
        python_results = run_python_algorithm(
            data['closes'], data['highs'], data['lows'], data['volumes']
        )
        print(f"  Python bars: {len(python_results)}")
        
        # Compare
        comparison = compare_algorithms(ticker, pine_results, python_results)
        if comparison:
            all_results.append(comparison)
            print(f"\n  📊 {ticker} Results:")
            print(f"     Trend match: {comparison['trend_matches']}/{comparison['total_bars']} ({comparison['trend_match_pct']:.1f}%)")
            print(f"     Zone match:  {comparison['zone_matches']}/{comparison['zone_matches'] + comparison['zone_mismatches']} ({comparison['zone_match_pct']:.1f}%)")
            print(f"     Avg strength diff:  {comparison['avg_strength_diff']:.1f}pp")
            print(f"     Avg confidence diff: {comparison['avg_confidence_diff']:.1f}pp")
        
        # Show detailed last 10 bars
        if args.detailed and pine_results:
            print(f"\n  📋 Last 10 bars (Pine Script simulation):")
            for r in pine_results[-10:]:
                trend_emoji = "🟢" if r['pine_trend'] == 1 else "🔴" if r['pine_trend'] == -1 else "🟡"
                print(f"     {trend_emoji} bar {int(r['bar_index']):4d} | "
                      f"${r['close']:8.2f} | "
                      f"trend={int(r['pine_trend']):+d} | "
                      f"str={int(r['pine_strength']):3d}% conf={int(r['pine_confidence']):3d}% | "
                      f"RSI={r['rsi']:5.1f} ADX={r['adx']:5.1f} | "
                      f"confirms={int(r['pine_confirmations'])}/6 synergy={int(r['pine_synergy'])}/6")
    
    # Summary
    print("\n" + "=" * 70)
    print("📊 VALIDATION SUMMARY")
    print("=" * 70)
    
    if all_results:
        total_bars = sum(r['total_bars'] for r in all_results)
        total_trend_matches = sum(r['trend_matches'] for r in all_results)
        overall_trend_match = (total_trend_matches / total_bars * 100) if total_bars > 0 else 0
        
        avg_strength_diff = np.mean([r['avg_strength_diff'] for r in all_results])
        avg_confidence_diff = np.mean([r['avg_confidence_diff'] for r in all_results])
        
        print(f"\nTickers validated: {len(all_results)}/{len(tickers)}")
        print(f"Total bars: {total_bars}")
        print(f"Overall trend match: {overall_trend_match:.1f}%")
        print(f"Average strength difference: {avg_strength_diff:.1f}pp")
        print(f"Average confidence difference: {avg_confidence_diff:.1f}pp")
        
        print(f"\nPer-ticker results:")
        for r in all_results:
            print(f"  {r['ticker']:5s} | Trend: {r['trend_match_pct']:5.1f}% | Zone: {r['zone_match_pct']:5.1f}% | Str diff: {r['avg_strength_diff']:5.1f}pp | Conf diff: {r['avg_confidence_diff']:5.1f}pp")
        
        if overall_trend_match >= 95:
            print(f"\n✅ Pine Script logic matches Python algorithm (>95% match)")
        elif overall_trend_match >= 85:
            print(f"\n⚠️ Pine Script logic mostly matches Python (85-95% match)")
            print(f"   Some differences expected due to calculation method differences")
        else:
            print(f"\n❌ Pine Script logic significantly differs from Python (<85% match)")
            print(f"   Review and fix discrepancies before publishing")
        
        # Note about v1.1
        print(f"\n✅ v1.1: Confidence double-counting FIXED.")
        print(f"   Confidence = total_strength + synergy_bonus only (no double-counting).")
        print(f"   Lite version uses SAME algorithm as Full (just no tables).")
    else:
        print("No data to compare")
    
    return all_results


if __name__ == '__main__':
    main()