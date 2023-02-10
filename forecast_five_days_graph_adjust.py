import requests, json
import my_owm_key as my
from datetime import datetime, timedelta, timezone
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#URLを作成する（東京の5日間天気予報）
city = "Tokyo,JP"
key = my.key
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"

#WebサーバにアクセスしてJSONデータを読み込む
jsondata = requests.get(url).json()

#空のDataFrameを作成する（項目名：気温）
df = pd.DataFrame(columns=["気温"])
jst = timezone(timedelta(hours=+9), "JST")

#5日間の天気予報データの表を作成する
for data in jsondata["list"]:
    jst_time = str(datetime.fromtimestamp(data["dt"], jst))[:-9]
    df.loc[jst_time] = data["main"]["temp"]

#表をグラフ化（折れ線グラフ）して表示する
df.plot(figsize=(15,8))
plt.ylim(-10,40)
plt.grid()
plt.show()
