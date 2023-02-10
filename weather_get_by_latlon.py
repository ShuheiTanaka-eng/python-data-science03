import requests, json
import my_owm_key as my

#URLを作成する（TOUの緯度経度）
lat, lon = 35.69158, 139.69696
key = my.key
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&lang=ja&units=metric"

#WebサーバにアクセスしてJSONデータを読み込む
jsondata = requests.get(url).json()

#都市名、気温、天気、天気詳細を出力する
print("都市名　：", jsondata["name"])
print("気温　　：", jsondata["main"]["temp"], "℃")
print("天気　　：", jsondata["weather"][0]["main"])
print("天気詳細：", jsondata["weather"][0]["description"])
