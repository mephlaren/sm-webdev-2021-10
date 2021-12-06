import json
#urllib: elképesztő hasznos vanilla url hívásokhoz, ennél erősebb megoldásokhoz viszont a
#requests használata ajánlott
from urllib.request import urlopen

#params
api_key = '716b45ef30e4417b053b374fb840e8b3'
city_name = 'Budapest,HU'
unit = 'metric'
#api call base
url_base = 'https://api.openweathermap.org/data/2.5'
#call
url = f"{url_base}/weather?q={city_name}&unit={unit}&appid={api_key}"

packet = urlopen(url).read()
weather_dict = json.loads(packet)
print(weather_dict["weather"][0]["description"])