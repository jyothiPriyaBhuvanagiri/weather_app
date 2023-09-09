import requests

params = {
    "access_key": "48a312bda934e0015b271f1c043f8158",
    "query": "Germany"
}

api_result = requests.get('http://api.weatherstack.com/current', params=params)

api_response = api_result.json()

# Print the full URL including query parameters
print("the current weather ="  ,api_response['current']['weather_code'])


