import requests, json
import my_owm_key as my
from datetime import datetime, timedelta, timezone

#URLを作成する
city = "Tokyo,JP"
key = my.key
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"

#WebサーバにアクセスしてJSONデータを読み込む
jsondata = requests.get(url).json()

#1件目の日時と天気詳細と気温とタイムスタンプを出力する
print("都市名　：", jsondata["city"]["name"])
data = jsondata["list"][0]

#UTCのタイムスタンプをJSTの時刻（文字列）に変換する
jst = timezone(timedelta(hours=+9), "JST")
jst_time = datetime.fromtimestamp(data["dt"], jst)

#1件目の日時（JST）、天気詳細、気温を出力する
print("日時　　：", str(jst_time)[:-9])
print("天気詳細：", data["weather"][0]["description"])
print("気温　　：", data["main"]["temp"], "℃")
