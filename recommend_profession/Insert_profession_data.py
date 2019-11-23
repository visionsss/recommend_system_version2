import pandas as pd
import sqlite3


if __name__ == '__main__':
    df = pd.read_csv('./profession.csv', encoding='GBK')
    df.iloc[:, 1] = df.iloc[:, 1].apply(lambda x: x.split("：")[-1])
    df.iloc[:, -1] = df.iloc[:, -1].apply(lambda x: x.split("（")[0])
    conn = sqlite3.connect("../db.sqlite3")
    cursor = conn.cursor()
    for i in range(len(df)):
        a = df.iloc[i, 1]
        b = df.iloc[i, 2]
        c = df.iloc[i, 3]
        print(a, b, c)
        sql = "insert into recommend_profession_profession values ('%d','%s','%s', '%s')" % (i, a, b, c)
        x = cursor.execute(sql)

    conn.commit()
