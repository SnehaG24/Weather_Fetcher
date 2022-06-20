import apikey
import requests

API_KEY = apikey.api_key()

Base_url = "http://api.openweathermap.org/data/2.5/weather"

city_name = input("Enter a City Name: ")   #userinput

request_url = f"{Base_url}?appid={API_KEY}&q={city_name}"

response = requests.get(request_url)

if response.status_code == 200 :

    data = response.json()
    
    # print(data)

    weather = data['weather'][0]['description']

    temperature =  round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)

    print("Temperature:", temperature,"celsius")

else:
    print("An error occurred.")
