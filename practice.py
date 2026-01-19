basic format

url = ddddddd
print(f"URL: {url_valid}")   #checking this lines whether URL is valid or not 
print(f"Status Code: {response.status_code}")
print(f"Success? {response.status_code == 200}") or  if response.status_code == 200:

response = requests.get(url)  #imp

data = response.json()   #fetching the data from url

print(f"Full Name: {data['name']}")    # perrform the certain operations
print(f"Username: {data['username']}")
print(f"Email: {data['email']}")
print(f"City: {data['address']['city']}")

