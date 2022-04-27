import requests
import os
from twilio.rest import Client

account_sid = 'AC6a047d46063858cd531c43153fcf51a9'
auth_token = 'dbd663ab5bf6f7050bd0b2b84e39c77f'

api_key = "5ae4aa7b9bb69c5470263503e4ef86bc"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 47.663452,
    "lon": 26.273230,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
hourly_list = []
for i in range(0,12):
    hourly_list.append(weather_data['hourly'][i]['weather'][0])

will_rain = False
for hour in hourly_list:
    if hour['id']<800:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Is rainny today, you better get an umbrella ☂️.",
        from_='+14793646388',
        to='+400771435128'
    )

    print(message)