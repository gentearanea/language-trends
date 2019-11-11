import matplotlib.pyplot as plt
from pytrends.request import TrendReq
from datetime import datetime
import json
import pandas as pd
import pprint

# プログラミング言語の人気度を取得
pytrends = TrendReq(hl='ja-JP', tz=360)
kw_list = ["Java","Python","Ruby","Javascript","PHP"]
pytrends.build_payload(kw_list, timeframe='today 5-y', geo='JP')
interest_over_time_df = pytrends.interest_over_time()
print(interest_over_time_df)

# 可視化
interest_over_time_df.plot(figsize=(10, 2))
plt.savefig('./test.png')
plt.close('all')

# pandasからjsonへ変換
# interest_over_time_json = interest_over_time_df.to_json()
# print(interest_over_time_json)
