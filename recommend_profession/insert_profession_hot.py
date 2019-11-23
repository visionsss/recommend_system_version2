import sqlite3
import pandas as pd
import numpy as np


conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()
data = pd.read_csv('./profession_hot.csv', encoding='GBK')
for i in range(1, len(data)):
    sql = "insert into recommend_profession_profession_hot values ('%d','%s','%s','%s')" \
          % (
              i,
              data.iloc[i, 1],
              data.iloc[i, 5],
              data.iloc[i, 7],
             )
    x = cursor.execute(sql)
    print(sql)
conn.commit()