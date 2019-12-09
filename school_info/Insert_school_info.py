# import sqlite3
# import pandas as pd
# import numpy as np
#
#
# conn = sqlite3.connect("../db.sqlite3")
# cursor = conn.cursor()
# data = pd.read_csv('./s.csv')
# for i in range(1, len(data)):
#     if str(data.iloc[i, 2]) == 'nan':
#         data.iloc[i, 2] = ' '
#     sql = "insert into school_info_school_info values ('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
#           % (
#               i,
#               data.iloc[i, 1],
#               data.iloc[i, 2],
#               data.iloc[i, 3],
#               data.iloc[i, 4],
#               data.iloc[i, 5],
#               data.iloc[i, 6],
#               data.iloc[i, 7],
#               data.iloc[i, 9],
#               int(data.iloc[i, 10]),
#               data.iloc[i, 8],
#              )
#     if data.iloc[i, 8] == '文科' or data.iloc[i, 8] == '理科':
#         x = cursor.execute(sql)
#     print(sql)
# # conn.commit()
# import sqlite3
# import pandas as pd
# import numpy as np
#
#
# conn = sqlite3.connect("../db.sqlite3")
# cursor = conn.cursor()
# data = pd.read_csv('./2014-2018大学分数线newdatas.csv')
# for i in range(0, len(data)):
#
#     sql = "insert into school_info_one_school values ('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
#           % (
#               i,
#               data.iloc[i, 1],
#               data.iloc[i, 2],
#               data.iloc[i, 3],
#               data.iloc[i, 4],
#               data.iloc[i, 5],
#               data.iloc[i, 6],
#               data.iloc[i, 7],
#               data.iloc[i, 9],
#               int(data.iloc[i, 10]),
#               data.iloc[i, 8],
#              )
#     if data.iloc[i, 8] == '文科' or data.iloc[i, 8] == '理科':
#         x = cursor.execute(sql)
#     print(sql)
# conn.commit()

import sqlite3
import pandas as pd
import numpy as np
from glob import glob
import base64

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()
path = r'D:\Note\大四\高考推荐系统\学校分数线折线图2014-2018\*'
for pic in glob(path):
    school_name = pic.split('\\')[-1].replace('分数线.jpg', '')
    with open(pic, 'rb') as f:
        print(school_name)
        res = base64.b64encode(f.read())
        sql = f"update school_info_one_school set pictures = '{res}' where school_name = '{school_name}'"
        # sql = f"select * from school_info_one_school where school_name='{school_name}'"
        try:
            x = cursor.execute(sql)
        except:
            print(sql)
            print('error')
#
#     sql = "insert into school_info_school_score values ('%d','%s','%s')" \
#           % (
#               i,
#               data.iloc[i, 0],
#               data.iloc[i, 16],
#
#              )
#     print(sql)
# conn.commit()