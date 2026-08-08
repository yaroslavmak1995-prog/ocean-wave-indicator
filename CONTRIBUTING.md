# Contributing to Ocean Wave

First off, thanks for taking the time to contribute! 🌊

This project is an open-source trading visualization indicator. We welcome contributions of all kinds — code, documentation, bug reports, feature ideas, backtest results.

## Ways to Contribute

### 🐛 Report Bugs
- Open an [issue](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues/new)
- Include: ticker, timeframe, screenshot, expected vs actual behavior
- Check existing issues first to avoid duplicates

### 💡 Suggest Features
- Open a [discussion](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions/6) in "Feature Requests for v3"
- Or open an issue with the `enhancement` label

### 📊 Share Backtest Results
- Post in the [Backtest Results discussion](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions/7)
- Include: ticker, timeframe, date range, win rate, observations

### 📝 Improve Documentation
- Good first issues are labeled [`good first issue`](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/labels/good%20first%20issue)
- Fix typos, add examples, improve clarity

### 💻 Write Code

#### Pine Script
- Main indicator: `pine/ocean-wave-v2.1.pine`
- Lite version: `pine/ocean-wave-lite-v2.1.pine`
- Test on [TradingView](https://www.tradingview.com/) before submitting

#### Python
- Reference algorithm: `python/nonuple_algorithm.py`
- Validation: `python/validate_pine_csv.py`

#### Web App (React)
- Repo: [ocean-view-app](https://github.com/yaroslavmak1995-prog/ocean-view-app)
- Deployed: [ocean-view-app.pages.dev](https://yaroslavmak1995-prog.github.io/ocean-view-app/)

## Development Setup

```bash
# Clone the repo
git clone https://github.com/yaroslavmak1995-prog/ocean-wave-indicator.git
cd ocean-wave-indicator

# Validate Pine Script against Python algorithm
python python/validate_pine_csv.py
```

## Pull Request Process

1. Create a branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test thoroughly (Pine Script: test on TradingView; Python: run validation)
4. Commit with clear messages: `git commit -m "Add: confidence EMA smoothing option"`
5. Open a Pull Request
6. Link any relevant issues: `Closes #123`

## Code Style

### Pine Script
- Use `camelCase` for variable names
- Comment sections with `// === Section Name ===`
- Keep indicator inputs grouped at the top
- Include `//@version=5` as first line

### Python
- Follow PEP 8
- Type hints encouraged
- Docstrings for public functions

## License

By contributing, you agree that your contributions will be licensed under the [Mozilla Public License 2.0](LICENSE).

## Questions?

- 💬 [GitHub Discussions](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/discussions) — ask anything
- 🐛 [Issues](https://github.com/yaroslavmak1995-prog/ocean-wave-indicator/issues) — bugs and features

---

Built with ❤️ by the Ocean View team. Not financial advice. DYOR.