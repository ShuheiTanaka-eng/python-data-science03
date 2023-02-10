import requests, json
import my_owm_key as my
from pprint import pprint

#URLを作成する
city = "Tokyo,JP"
key = my.key
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=ja&units=metric"

#WebサーバにアクセスしてJSONデータを読み込む
jsondata = requests.get(url).json()

#JSONデータを整形して出力する
pprint(jsondata)
