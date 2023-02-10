import requests, json
import my_owm_key as my
from datetime import datetime, timedelta, timezone

#URLを作成する（東京の5日間天気予報）
city = "Tokyo,JP"
key = my.key
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"

#WebサーバにアクセスしてJSONデータを読み込む
jsondata = requests.get(url).json()

#都市名の表示と、タイムゾーンの設定をする
print(f'{jsondata["city"]["name"]}の5日間天気予報')
jst = timezone(timedelta(hours=+9), "JST")

#5日間の天気予報データを出力する
for data in jsondata["list"]:
    print("----------------------------")
    jst_time = datetime.fromtimestamp(data["dt"], jst)
    print("日時　　：", str(jst_time)[:-9])
    print("天気詳細：", data["weather"][0]["description"])
    print("気温　　：", data["main"]["temp"], "℃")
