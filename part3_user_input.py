"""
Part 3: Dynamic Queries with User Input
=======================================
Difficulty: Intermediate

Learn:
- Using input() to make dynamic API requests
- Building URLs with f-strings
- Query parameters in URLs
"""

import requests


def get_user_info():
    """Fetch user info based on user input."""
    print("=== User Information Lookup ===\n")

    user_id = input("Enter user ID (1-10): ")

    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\n--- User #{user_id} Info ---")
        print(f"Name: {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Website: {data['website']}")
    else:
        print(f"\nUser with ID {user_id} not found!")


def search_posts():
    # """Search posts by user ID."""
    user_id = input("Enter user ID (1 to 10): ")

    url = "https://jsonplaceholder.typicode.com/posts"

    params={"userId": user_id}  # use to filter the APIs
            
    response = requests.get(url, params)

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])
    else:
        print("Error fetching posts")

# def search_posts():
#     """Search posts by user ID."""
#     print("\n=== Post Search ===\n")

#     user_id = input("Enter user ID to see their posts (1-10): ")

    # Using query parameters
    
    # url = "https://jsonplaceholder.typicode.com/posts"
    # params = {"userId": user_id}

    # response = requests.get(url, params=params)
    # posts = response.json()

    # if posts:
    #     print(f"\n--- Posts by User #{user_id} ---")
    #     for i, post in enumerate(posts, 1):
    #         print(f"{i}. {post['title']}")
    # else:
    #     print("No posts found for this user.")


def get_crypto_price():
    """Fetch cryptocurrency price based on user input."""
    print("\n=== Cryptocurrency Price Checker ===\n")

    print("Available coins: btc-bitcoin, eth-ethereum, doge-dogecoin")
    coin_id = input("Enter coin ID (e.g., btc-bitcoin): ").lower().strip()

    url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        price_usd = data['quotes']['USD']['price']
        change_24h = data['quotes']['USD']['percent_change_24h']

        print(f"\n--- {data['name']} ({data['symbol']}) ---")
        print(f"Price: ${price_usd:,.2f}")
        print(f"24h Change: {change_24h:+.2f}%")
    else:
        print(f"\nCoin '{coin_id}' not found!")
        print("Try: btc-bitcoin, eth-ethereum, doge-dogecoin")


def main():
    """Main menu for the program."""
    print("=" * 40)
    print("  Dynamic API Query Demo")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Look up user info")
        print("2. Search posts by user")
        print("3. Check crypto price")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ")

        if choice == "1":
            get_user_info()
        elif choice == "2":
            search_posts()
        elif choice == "3":
            get_crypto_price()
        elif choice == "5":
            get_city_name()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# --- EXERCISES ---
#
# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)
#
# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false
#
# Exercise 3: Add input validation (check if user_id is a number)


#Exercise 1
def get_city_name():
    city = input("Please enter the city name: ")

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if "results" in data:
            latitude = data["results"][0]["latitude"]
            longitude = data["results"][0]["longitude"]

            print("City:", city)
            print("Latitude:", latitude)
            print("Longitude:", longitude)
        else:
            print("City not found ❌")
    else:
        print("API Error ❌")


        
# get_city_name()

# Exercise 2: Add a function to search todos by completion status
#             URL: https://jsonplaceholder.typicode.com/todos
#             Params: completed=true or completed=false

def search_todos_by_status():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()   # This is a LIST

        user_input = input("Enter completed status (true/false): ").lower()

        # Convert string to boolean
        if user_input == "true":
            status = True
        elif user_input == "false":
            status = False
        else:
            print("Invalid input ❌")
            return

        print("\nMatching Todos:\n")

        for todo in todos:
            if todo["completed"] == status:
                print(f"ID: {todo['id']} | Title: {todo['title']}")

    else:
        print("API request failed ❌")



#Exercise 3: Add input validation (check if user_id is a number)

def search_todos_by_user_id():
    user_id = input("Enter user ID: ")

    # Input validation
    if not user_id.isdigit():
        print("Invalid input ❌ User ID must be a number")
        return

    user_id = int(user_id)   # convert AFTER validation

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()

        print(f"\nTodos for user ID {user_id}:\n")

        for todo in todos:
            if todo["userId"] == user_id:
                print(f"ID: {todo['id']} | Title: {todo['title']} | Completed: {todo['completed']}")
    else:
        print("API Error ❌")



  