import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "fb423834d3fc46f38754a0ce8d452535"

weather_params = {
    "lat": -20.326280,
    "lon": -40.391820,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWN_Endpoint, params=weather_params)

response.raise_for_status()

weather_data = response.json()

will_rain = False
for num_list in weather_data["list"]:
    condition_code = num_list["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        break
    
if will_rain:
    print("Bring an umbrella.")