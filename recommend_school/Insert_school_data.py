import pandas as pd
import sqlite3


if __name__ == '__main__':
    df = pd.read_csv('./广东.csv', encoding='GBK')
    print(df.head(5))
    conn = sqlite3.connect("../db.sqlite3")
    cursor = conn.cursor()
    df = df.fillna(value='--')
    for i in range(len(df)):
        a = int(df.iloc[i, 0])
        b = df.iloc[i, 1]
        c = df.iloc[i, 2]
        d = df.iloc[i, 3]
        e = df.iloc[i, 4]
        f = df.iloc[i, 5]
        g = df.iloc[i, 6]
        h = df.iloc[i, 7]
        i = df.iloc[i, 8]
        print(a, b, c,d,e,f,g,h)
        sql = "insert into recommend_school_re_school values ('%d','%s','%s', '%s','%s','%s', '%s', '%s','%s')" % (a, b, c,d,e,f,g,h,i)
        x = cursor.execute(sql)

    conn.commit()