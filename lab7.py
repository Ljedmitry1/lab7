
import requests
city, key = "Санкт-Петербург", "83a3df76f0df99b10972f58aef916709"
data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric&lang=ru").json()
print(f"{city}: {data['main']['temp']}°C, влажность {data['main']['humidity']}%, давление {data['main']['pressure']} гПа")