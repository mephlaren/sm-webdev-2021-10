import json
from urllib.request import urlopen
import time
from datetime import datetime
#PROGRAM: egy olyan program, ami dinamikusan x időközönként lekéri városok időjárásadatát
#és kiszámolja, hogy a repülőgép le tud-e szállni a városban az időjárási viszonyok között

#params
api_key = '716b45ef30e4417b053b374fb840e8b3'
unit = 'metric'
#api call base
url_base = 'https://api.openweathermap.org/data/2.5/weather?'

#repülési paraméterek
max_w_speed = 2.0
#program paraméterek
sleep_timer = 3
cities = [
            "Budapest,HU",
            "London,UK",
            "Rome,IT",
            "Hamburg,DE",
            "Berlin,DE",
            "Paris,FR",
            "Bangkok,TH"
         ]
clean_data = {}
filtered_data = {}

def get_wind_data(city):
    url = f"{url_base}appid={api_key}&units={unit}&q={city}"
    packet = urlopen(url).read()
    return json.loads(packet)["wind"]

def get_city_data():
    for city in cities:
        clean_data[city] = get_wind_data(city)

def analyze_cities():
    get_city_data()
    for varos, szel_adat in clean_data.items():
        if szel_adat["speed"] <= max_w_speed:
            filtered_data[varos] = szel_adat

while True:
    analyze_cities()
    print(f"{datetime.now()} ADAT:")
    for varos, ertekek in filtered_data.items():
        print(f"\t{varos}-ban a szélsebesség megfelelő.\n"
              f"\t\t->windspeed: {ertekek['speed']} kts, direction: {ertekek['deg']} deg")
    print("========END OF REPORT===========\n")
    time.sleep(sleep_timer)



