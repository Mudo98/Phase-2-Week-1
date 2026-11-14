# AI Master Class - Phase 2 Week 1: API Integration

> Learning how to connect Python code to the real world using public APIs.

This repository contains my daily practice and final project for Phase 2, Week 1. The focus was on `requests`, handling JSON, environment variables, and error handling.

### 🚀 Final Project: KES Currency Converter

**File:** `week1_project.py`

A live currency converter that uses **KES (Kenyan Shilling)** as base currency and converts a given amount (e.g., KES 20) into USD, EUR, GBP and other major currencies.

- **Live API:** `https://open.er-api.com/v6/latest/KES` (Free, no key required)
- **Features:**
    - Fetches real-time rates
    - Clean formatted table output
    - Shows last updated timestamp
    - Handles network errors & API errors gracefully

**Run it:**
```bash
pip install -r requirements.txt
python week1_project.py