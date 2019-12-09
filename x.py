# -*- coding:utf-8 -*-
from glob import glob
import pandas as pd
import numpy as np
import sqlite3
if __name__ == '__main__':
    paths = r'C:\Users\Administrator\Desktop\学校专业信息.csv'
    conn = sqlite3.connect(r"./db.sqlite3")
    cursor = conn.cursor()
    df = pd.read_csv(paths, encoding='GBK')
    for i in range(len(df)):
        school_name = df.iloc[i, 2]
        profession_name = df.iloc[i, 3].replace('\'', '')
        student_type = df.iloc[i, 4]
        year = df.iloc[i, 5]
        top_score = df.iloc[i, 7]
        avg_score = df.iloc[i, 8]
        lowest_score = df.iloc[i, 9]
        lowest_rank = df.iloc[i, 10]
        epoch = df.iloc[i, 11]
        sql = "insert into school_info_one_school values ('%d','%s','%s','%s','%s','%s','%s','%s','%s', '%s')" \
              % (
                  i,
                  school_name,
                  profession_name,
                  student_type,
                  year,
                  top_score,
                  avg_score,
                  lowest_score,
                  lowest_rank,
                  epoch,
              )
        try:
            cursor.execute(sql)
        except:
            print(sql)
    conn.commit()
