import requests


def fetch_user_summary():
    # URL targeting a specific user profile (User ID 1)
    url = "https://typicode.com"

    try:
        # Fetch live data from the API
        response = requests.get(url)

        # Raise an exception for HTTP errors (e.g., 404, 500)
        response.raise_for_status()

        # Parse the JSON response body into a Python dictionary
        user_data = response.json()

        # Extract specific data points cleanly
        name = user_data.get("name", "N/A")
        username = user_data.get("username", "N/A")
        email = user_data.get("email", "N/A")

        # Safely extract values from nested dictionaries
        address_info = user_data.get("address", {})
        city = address_info.get("city", "N/A")
        street = address_info.get("street", "N/A")

        company_info = user_data.get("company", {})
        company_name = company_info.get("name", "N/A")

        # Print a clean, beautifully formatted human-readable summary
        print("=" * 40)
        print("       LIVE USER PROFILE SUMMARY        ")
        print("=" * 40)
        print(f"Full Name:     {name}")
        print(f"Username:      @{username}")
        print(f"Email Address: {email}")
        print("-" * 40)
        print("LOCATION DETAILS")
        print(f"Street:        {street}")
        print(f"City:          {city}")
        print("-" * 40)
        print("EMPLOYMENT DETAILS")
        print(f"Company:       {company_name}")
        print("=" * 40)

    except requests.exceptions.RequestException as error:
        print(f"Error connecting to the live API source: {error}")


if __name__ == "__main__":
    fetch_user_summary()
