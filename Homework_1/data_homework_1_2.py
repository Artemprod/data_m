import requests
from pprint import pprint
import math


def get_weather(city_name):
    API_KEY = 'a26f9aea9feedfddb40dcb0c70c6540a'
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

    req = requests.get(URL)
    req_dict = dict(req.json())

    temperature_info = dict(req_dict.get('main'))
    wind_info = dict(req_dict.get('wind'))
    weather_con_list = (req_dict.get('weather', ))
    weather_con_dict = dict(weather_con_list[0])
    result = f" Temperature in  {city_name} is {math.ceil(temperature_info.get('temp'))} degrees to Kelvin but it feels like " \
             f"{math.ceil(temperature_info.get('feels_like'))} and wind's speed {wind_info.get('speed')} m.\s. " \
             f" Average temperature per day is {math.ceil((temperature_info.get('temp_min') + temperature_info.get('temp_max')) / 2)}" \
             f" and if you are going " \
             f"out of the home you will see {weather_con_dict.get('description')}.  "
    print(result)
    return result


city_name = str(input("Input city name: "))
get_weather(city_name)
