# AI Master Class - Phase 2 Week 1: API Integration

Building real-world AI tools with Python and public APIs.

## 🚀 What I Built

**Day 1: API Fundamentals (`day1_api.py`)**
- HTTP requests with Python `requests`
- Error handling and response parsing

**Day 2: Weather Tool (`day2_weather.py`)**
- OpenWeatherMap API integration
- Real-time weather by city name
- Secure API keys with `.env`

**Day 3: Travel Intelligence Tool (`day3_travel_info.py`)**
- Input any city: `Kyotera`, `Kampala`, `Beijing`
- Output: Weather, Region, Population, Currency, Coordinates
- Chained 2 APIs: OpenWeather + REST Countries
- Handled real-world API deprecation (v3.1 -> v5)

## 🛠️ Tech Stack
Python, requests, python-dotenv, OpenWeatherMap API, REST Countries API, Git/GitHub

## ⚙️ How to Run
```bash
git clone https://github.com/Mudo98/Phase-2-Week-1.git
cd Phase-2-Week-1
# Create .env file with your keys
# OPENWEATHER_API_KEY=your_key
# RESTCOUNTRIES_API_KEY=your_key
pip install requests python-dotenv
python day3_travel_info.py
