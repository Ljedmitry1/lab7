import requests

API_KEY = "EB17D4A2756CA987AD792CBA03E11E38"  
STEAM_ID = "76561199112420966" 

url = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={STEAM_ID}"
response = requests.get(url)
data = response.json()

player = data['response']['players'][0]
print(f"Никнейм: {player['personaname']}")
print(f"Реальное имя: {player.get('realname', 'Не указано')}")
print(f"Страна: {player.get('loccountrycode', 'Не указана')}")
print(f"Статус: {'В сети' if player.get('personastate') == 1 else 'Не в сети'}")
print(f"Профиль: {player['profileurl']}")
print(f"Аватар: {player['avatarfull']}")
