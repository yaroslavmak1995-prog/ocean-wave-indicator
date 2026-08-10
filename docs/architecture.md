# 🏗️ Architecture Diagram

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     OCEAN WAVE SYSTEM                            │
└─────────────────────────────────────────────────────────────────┘

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │   TRADINGVIEW │     │   WEB APP    │     │   GITHUB     │
  │  (Pine Script)│     │  (React SPA) │     │  (Repo + API)│
  └──────┬───────┘     └──────┬───────┘     └──────┬───────┘
         │                    │                    │
         │                    │                    │
         ▼                    ▼                    ▼
  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  Pine Editor  │     │  GitHub Pages │     │  GitHub API  │
  │  v2.1 Full    │     │  ocean-view-  │     │  Issues      │
  │  v2.1 Lite    │     │  app          │     │  Discussions │
  │  11 alerts    │     │  (HTTP 200)   │     │  Releases    │
  └──────┬───────┘     └──────┬───────┘     └──────────────┘
         │                    │
         │                    │ REST API
         │                    ▼
         │             ┌──────────────┐
         │             │  FastAPI     │
         │             │  Backend     │
         │             │  (Railway)   │
         │             │  v1.4.0      │
         │             └──────┬───────┘
         │                    │
         │                    │ yfinance
         │                    ▼
         │             ┌──────────────┐
         │             │  Yahoo Finance│
         │             │  (Market Data)│
         │             └──────────────┘
         │
         ▼
  ┌──────────────────────────────────────────┐
  │        9-FACTOR ALGORITHM                 │
  │                                           │
  │  ┌─────┐ ┌──────┐ ┌─────┐ ┌─────┐        │
  │  │ MA  │ │ Vol  │ │ Mom │ │ RSI │        │
  │  │20/50│ │ Conf │ │ Chk │ │ 14  │        │
  │  └──┬──┘ └──┬───┘ └──┬──┘ └──┬──┘        │
  │     │       │        │       │            │
  │  ┌──┴──┐ ┌──┴───┐ ┌──┴──┐ ┌─┴───┐        │
  │  │ ADX │ │ MACD │ │ ATR │ │ Boll│        │
  │  │ 14  │ │12/26 │ │ 14  │ │ 20  │        │
  │  └──┬──┘ └──┬───┘ └──┬──┘ └──┬──┘        │
  │     │       │        │       │            │
  │     └───────┴───┬────┴───────┘            │
  │                 │                         │
  │          ┌──────┴──────┐                  │
  │          │  Stochastic  │                  │
  │          │   14/3/3     │                  │
  │          └──────┬──────┘                  │
  │                 │                         │
  │     ┌───────────┴───────────┐             │
  │     │   SYNERGY BONUS        │             │
  │     │   4+ agree → +10 conf  │             │
  │     │   3+ → min 25% floor   │             │
  │     │   5+ → min 50% floor   │             │
  │     └───────────┬───────────┘             │
  │                 │                         │
  │     ┌───────────┴───────────┐             │
  │     │  CONFIDENCE SMOOTHING  │             │
  │     │  (EMA-based, v2.1)     │             │
  │     └───────────┬───────────┘             │
  │                 │                         │
  │     ┌───────────┴───────────┐             │
  │     │     OUTPUT              │             │
  │     │  ┌─────────────────┐   │             │
  │     │  │ Zone: 🟢🟡🔴    │   │             │
  │     │  │ Confidence: 0-100│   │             │
  │     │  │ Strength: 0-100  │   │             │
  │     │  │ 9 Factor Table   │   │             │
  │     │  │ Signal Label     │   │             │
  │     │  └─────────────────┘   │             │
  │     └─────────────────────────┘            │
  └──────────────────────────────────────────┘
```

## Data Flow

```
User (Trader)
  │
  ├──► TradingView chart
  │      └──► Pine Script v2.1 runs locally in TV
  │            └──► 9 indicators calculated on chart data
  │                  └──► Colored zone + confidence rendered
  │
  ├──► Web App (browser)
  │      └──► React frontend (GitHub Pages)
  │            └──► Fetch to FastAPI backend (Railway)
  │                  └──► yfinance → Yahoo Finance API
  │                        └──► JSON response → React renders table
  │
  └──► GitHub repo
         └──► Pine Script source code
         └──► Python reference implementation
         └──► Backtest results (JSON)
         └──► Documentation (algorithm, configs, results)
```

## Tech Stack

| Component | Technology | Hosting |
|-----------|-----------|---------|
| Pine Script | TradingView Pine v5 | TradingView |
| Frontend | React + Vite | GitHub Pages |
| Backend | FastAPI + yfinance | Railway |
| Version Control | Git | GitHub |
| Issues/Discussions | GitHub native | GitHub |
| Release | GitHub Releases | GitHub |
| License | MPL 2.0 | — |

## Deployment

```
GitHub Push ──► GitHub Pages (auto-deploy)
           ──► Railway (auto-deploy from main branch)
           ──► TradingView (manual: copy Pine Script to editor)
```