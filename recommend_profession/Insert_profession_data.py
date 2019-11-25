import pandas as pd
import sqlite3
import numpy as np
from sklearn.preprocessing import MinMaxScaler

if __name__ == '__main__':
    df = pd.read_csv('./major_data(6).csv', encoding='GBK')
    conn = sqlite3.connect("../db.sqlite3")
    cursor = conn.cursor()
    min_max = MinMaxScaler()
    x = np.array(df.iloc[:, 4]).reshape(-1, 1)
    min_max.fit_transform(x)
    df.iloc[:, 4] = min_max.transform(x)
    for i in range(len(df)):
        a = df.iloc[i, 1]
        b = df.iloc[i, 2]
        c = df.iloc[i, 3]
        d = df.iloc[i, 4]
        e = df.iloc[i, 5]
        print(d)
        d = int(d*1000)
        sql = "insert into recommend_profession_profession values ('%d','%s','%s', '%s', '%s', '%s')" % (i, a, b, c, d, e)
        print(sql)
        x = cursor.execute(sql)

    conn.commit()
