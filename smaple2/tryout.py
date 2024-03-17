import requests

url = "https://api.openweathermap.org/data/2.5/forecast"


params = {
    'q': 'bangalore',
    'appid': '13129000fa3d9c6f1cef8e8524284c07'
}

response = requests.get(url, params=params)
weather_details = response.json()
if response.status_code == 200:
    print("Received data from API:")
else:
    print("Failed to retrieve data from API. Status code:", response.status_code)
weather_data = [[]]

for i in range(0,40):
    weather_data[0].append(dict(date=weather_details["list"][i]["dt_txt"],
                             temparatures=round(weather_details["list"][i]["main"]["temp"]-273.15,2),
                             todays_forecast=weather_details["list"][i]["weather"][0]["main"],
                             description=weather_details["list"][i]["weather"][0]["description"],
                             humidity = weather_details["list"][i]["main"]["humidity"],
                             wind_speed = weather_details["list"][i]["wind"]["speed"]))
weather_data.append(params["q"])
print(weather_data[0][0])

