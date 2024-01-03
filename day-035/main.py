import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "fb423834d3fc46f38754a0ce8d452535"

weather_params = {
    "lat": -20.326280,
    "lon": -40.391820,
    "appid": api_key
}

response = requests.get(OWN_Endpoint, params=weather_params)

print(response.json())