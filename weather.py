# https://api.open-meteo.com/v1/forecast?latitude=20.59&longitude=78.96&hourly=weathercode&timezone=auto

# create a weather app that gives time using latitude and longitude  266fcbf5dc554182b14120006232208

import requests

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Banglore&units=imperial&APPID=266fcbf5dc554182b14120006232208")


weather = weather_data.json()['weather'][0]['main']
temperature = round(weather_data.json()['main']['temp'])
print(f"The weather is: {weather}")
print(f"The temperature inis: {temp}ºF")