import sqlite3
import pandas as pd
import numpy as np


conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()
data = pd.read_csv('./school_info.csv', encoding='GBK')
for i in range(1, len(data)):
    if str(data.iloc[i, 2]) == 'nan':
        data.iloc[i, 2] = ' '
    if data.iloc[i, 5] == 1:
        data.iloc[i, 5] = '是'
    else:
        data.iloc[i, 5] = '否'
    if data.iloc[i, 6] == 1:
        data.iloc[i, 6] = '是'
    else:
        data.iloc[i, 6] = '否'
    if data.iloc[i, 7] == 1:
        data.iloc[i, 7] = '是'
    else:
        data.iloc[i, 7] = '否'
    sql = "insert into school_info_school_info values ('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
          % (
              i,
              data.iloc[i, 1],
              data.iloc[i, 2],
              data.iloc[i, 3],
              data.iloc[i, 4],
              data.iloc[i, 5],
              data.iloc[i, 6],
              data.iloc[i, 7],
              data.iloc[i, 8],
              data.iloc[i, 9],
              data.iloc[i, 10],
             )
    x = cursor.execute(sql)
    print(sql)
conn.commit()
