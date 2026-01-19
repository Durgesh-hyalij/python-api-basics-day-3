#check the file name properly this means i make this code myself

import requests
from datetime import datetime

# ------------------ DATA ------------------

CITIES = {
    "delhi": (28.6139, 77.2090),
    "mumbai": (19.0760, 72.8777),
    "bangalore": (12.9716, 77.5946),
    "chennai": (13.0827, 80.2707),
    "kolkata": (22.5726, 88.3639),
    "hyderabad": (17.3850, 78.4867),
    "new york": (40.7128, -74.0060),
    "london": (51.5074, -0.1278),
    "tokyo": (35.6762, 139.6503),
    "sydney": (-33.8688, 151.2093),
     # newly added cities  #Exercise 1
    "pune": (18.5204, 73.8567),
    "nagpur": (21.1458, 79.0882),
    "nashik": (19.9975, 73.7898),
    "aurangabad": (19.8762, 75.3433)
}

CRYPTO_IDS = {
    "bitcoin": "btc-bitcoin",
    "ethereum": "eth-ethereum",
    "dogecoin": "doge-dogecoin",
    "cardano": "ada-cardano",
    "solana": "sol-solana",
    "ripple": "xrp-xrp",
}

# ------------------ COMMON API FUNCTION ------------------

def get_json(url, params=None):             #always write this code for make the url safe instead of url ="" then response = requests.get(url) 
    try:
        r = requests.get(url, params=params, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        print("API Error:", e)
        return None

# ------------------ WEATHER ------------------

def get_weather(city):
    city = city.lower().strip()

    if city not in CITIES:
        print("City not found")
        print("Available cities:", ", ".join(CITIES.keys()))
        # call open-netio api for city to lat,lon extraction
        # lat,lon = reponse from the api
    else:
        lat, lon = CITIES[city]

    return get_json(
        "https://api.open-meteo.com/v1/forecast",
        {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "timezone": "auto"
        }
    )
        
    


def display_weather(city):
    data = get_weather(city)
    if not data:
        return

    w = data["current_weather"]

    print("\nWeather in", city.title())
    print("Temperature:", w["temperature"], "°C")
    print("Wind Speed:", w["windspeed"], "km/h")

# ------------------ CRYPTO ------------------

def get_crypto(coin):
    coin = coin.lower().strip()
    coin_id = CRYPTO_IDS.get(coin, coin)
    return get_json(f"https://api.coinpaprika.com/v1/tickers/{coin_id}")

def display_crypto(coin):
    data = get_crypto(coin)
    if not data:
        return

    usd = data["quotes"]["USD"]

    print("\n", data["name"], f"({data['symbol']})")
    print("Price:", usd["price"])
    print("24h Change:", usd["percent_change_24h"], "%")

# ------------------ TOP CRYPTOS ------------------

def display_top_cryptos():
    data = get_json("https://api.coinpaprika.com/v1/tickers", {"limit": 5})
    if not data:
        return

    print("\nTop 5 Cryptos")
    for coin in data:
        print(coin["rank"], coin["name"], coin["quotes"]["USD"]["price"])

# ------------------ DASHBOARD ------------------

def dashboard():
    print("\nAPI Dashboard")
    print(datetime.now())

    while True:
        print("\n1. Weather")
        print("2. Crypto Price")
        print("3. Top 5 Cryptos")
        print("4. Quick (Delhi + Bitcoin)")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            display_weather(input("City: "))
        elif choice == "2":
            display_crypto(input("Crypto: "))
        elif choice == "3":
            display_top_cryptos()
        elif choice == "4":
            display_weather("delhi")
            display_crypto("bitcoin")
        elif choice == "5":
            break
        else:
            print("Invalid choice")

# ------------------ START ------------------

if __name__ == "__main__":
    dashboard()
