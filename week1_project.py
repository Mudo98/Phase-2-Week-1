import os
import sys
import requests

TARGET_CURRENCIES = ["USD", "EUR", "GBP"]

def get_kes_rates(api_key=None):
    """Fetches live exchange rates with KES as the base currency."""
    if api_key:
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/KES"
    else:
        # Open-access free endpoint (no API key required, updates once every 24h)
        url = "https://open.er-api.com/v6/latest/KES"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if data.get("result") != "success":
            error_type = data.get("error-type", "Unknown API error")
            print(f"API Error: {error_type}")
            sys.exit(1)

        return data["rates"], data.get("time_last_update_utc", "N/A")

    except requests.exceptions.RequestException as err:
        print(f"Network error while fetching rates: {err}")
        sys.exit(1)

def convert_price(kes_amount, rates):
    """Converts a KES amount into USD, EUR, and GBP."""
    conversions = {}
    for currency in TARGET_CURRENCIES:
        rate = rates.get(currency)
        if rate is not None:
            conversions[currency] = kes_amount * rate
    return conversions

def main():
    # Optional: Set EXCHANGERATE_API_KEY in your environment for higher rate limits
    api_key = os.getenv("EXCHANGERATE_API_KEY")

    # Accept amount via command-line argument or interactive prompt
    if len(sys.argv) > 1:
        raw_amount = sys.argv[1]
    else:
        raw_amount = input("Enter price in KES: ").strip()

    try:
        kes_amount = float(raw_amount.replace(",", ""))
        if kes_amount < 0:
            raise ValueError("Amount cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a valid positive number (e.g., 15000).")
        sys.exit(1)

    rates, last_updated = get_kes_rates(api_key)
    results = convert_price(kes_amount, rates)

    print("\n" + "=" * 42)
    print(f"  QUOTE CONVERSION FOR KES {kes_amount:,.2f}")
    print("=" * 42)
    for currency, value in results.items():
        rate = rates[currency]
        print(f"  {currency}: {value:>12,.2f}  (1 KES = {rate:.6f} {currency})")
    print("-" * 42)
    print(f"  Rates updated: {last_updated}")
    print("=" * 42 + "\n")

if __name__ == "__main__":
    main()
