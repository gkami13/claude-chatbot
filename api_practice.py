# import requests
# # Make a request to a simple API that returns random facts
# response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
# # Print what we got back
# print("Status Code:", response.status_code)
# print()
# print("Response Data:")
# print(response.text)

import requests
# Get a random fact
response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
# Check if the request worked
if response.status_code == 200:
# Convert JSON text to a Python dictionary
    data = response.json()
# Extract the fact from the data
    fact = data["text"]
    print("Random Fact:")
    print(fact)
else:
    print("Error: Could not get data from API")
    print("Status code:", response.status_code)