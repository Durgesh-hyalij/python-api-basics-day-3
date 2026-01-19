import requests

"""Fetch user info based on user input."""
def getuser_info():
    url = f"https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    
        print(data['name'])
        print(data['address']['street'])
    else:
        print(f"wrong status code: {response.status_code}")


def search_post():

    user_id  = input("Enter the user ID 1 to 10")
    url = f"https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, params = {"userId" : user_id})

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
           print(post['title'])

    else:
        print("Error fetching posts")

    
def get_crypto_price():
    user_input = input(print("Enter the value for crypto : "))
    url = f"https://api.coinpaprika.com/v1/tickers/{user_input}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        print(data['quotes']['USD']['price'])

    else:
        print("NO USER FOUND")
    

def whether():
    url = "https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true"
    response = requests.get(url)

    user_input = input("Enter the Input latitude and longitude")
    if response.status_code == 200:
        data = response.json()

           


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





# Exercise 1: Add a function to fetch weather for a city
#             Use Open-Meteo API (no key required):
#             https://api.open-meteo.com/v1/forecast?latitude=28.61&longitude=77.23&current_weather=true
#             Challenge: Let user input city name (you'll need to find lat/long)

def whether():
    city = input("Enter the city name: ")
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()


        if "results" in data:
            latitude = data["results"][0]["latitude"]
            longitude = data["results"][0]["longitude"]

            print(longitude)
        else:
            print("City not found")

    else:
        print("error in API")




def todo():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        for d in data:
            if d['completed'] == True:
                print(d['id'])
                print(d['title'])
            else:
                print("No data Found")

    else:
        print("Invalid API")

todo()