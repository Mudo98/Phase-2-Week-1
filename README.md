@'
# KES Live Converter — Phase 2 Week 1

Live KES → USD / EUR / GBP converter using exchangerate-api. Built for instant multi-currency quoting from a KES price.

### Live Output

### What It Does
- Fetches live exchange rates with KES as base currency
- Converts any KES amount to USD, EUR, GBP
- Shows both converted total and per-KES rate
- Works with or without API key

### Features
- Dual API Mode: Open endpoint (no key required) + Auth endpoint with higher limits
- Flexible Input: CLI argument or interactive prompt
- Input Sanitization: Handles commas, spaces, validates positive numbers
- Robust Error Handling: Network, API, and invalid input errors
- Timestamped Rates

### Tech Stack
- Python 3.x
- requests

### Quick Start

1. Clone
```bash
git clone https://github.com/Mudo98/Phase-2-Week-1.git
cd Phase-2-Week-1
