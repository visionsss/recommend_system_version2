# coding=utf-8
import csv

#数据文件路径
path = './school_info/分数线+评分2.csv'
with open(path, newline='', encoding='gbk') as csvfile:
    datas = list(csv.reader(csvfile))[1:]  #获取数据

datasSorted = sorted(datas,key=(lambda x : x[24]),reverse=True)   #数据按评分进行一次排序，由大到小，16是评分一栏的Index


def running(inputSchool,province):
    n0 = 10  #设置评分前面的长度
    n1 = 15  #后面的
    outputSchool0 = []  #保存排名靠前的
    outputSchool1 = []  #保存排名靠后的
    if province == '':  #如果不进行输入，默认为上面学校的省份
        province = [data[1] for data in datasSorted if inputSchool == data[0]][0]
    if province == '全国':
        schoolName = [x[0] for x in datasSorted]  # 找出所有的学校名字
        index = schoolName.index(inputSchool)  # 找出输入学校在数据中的Index

        # 输出评分排在输入学校前面的那些学校
        try:
            indexs = []
            for i in range(n0,0,-1):  #倒序减法
                indexs.append(index-i)  # 找出排在前面n0个的Index
            for i in indexs:  # 判断index的大学，避免类似清华大学这种前面没有其他学校的情况出现
                if i >= 0:
                    outputSchool0.append(schoolName[i])
        except:
            pass
        try:
            indexs = []
            for i in range(1,n1+1):  #正序加法
                indexs.append(index + i)  # 找出排在后面n1个的Index
            for i in indexs:  # 判断index的大学，避免类似最差学校这种后面没有其他学校的情况出现
                if i < len(schoolName):
                    outputSchool1.append(schoolName[i])
        except:
            pass

        # 输出具体推荐的学校
        print('\n在全国，评分在 ' + inputSchool + ' 前面的学校：', end='')  # 前面的学校
        if len(outputSchool0) == 0:  # 证明为空列表
            print('无')
        else:
            for each in outputSchool0:
                print(each,' ',end='')

        print('\n在全国，评分在 ' + inputSchool + ' 后面的学校是： ',end='')  # 后面的学校
        if len(outputSchool1) == 0:  # 证明为空列表
            print('无')
        else:
            for each in outputSchool1:
                print(each,' ',end='')


    else:
        school = [x for x in datasSorted if inputSchool == x[0]][0]   #找出输入学校的具体信息
        schools = [x for x in datasSorted if x[1] == province]  #找出当前省份的所有学校
        if school not in schools:  #判断输入的学校是否在这个省份的列表中，作用是进行评分的排序
            schools.append(school)  #加入学校，方便按评分排序
            schools = sorted(schools, key=(lambda x: x[24]), reverse=True)  # 数据按评分进行一次排序，由大到小，16是评分一栏的Index

        schoolName = [x[0] for x in schools]   #找出所有的学校名字
        index = schoolName.index(inputSchool)   #找出输入学校在数据中的Index

        #输出评分排在输入学校前面的那些学校
        try:
            indexs = []
            for i in range(n0, 0, -1):  # 倒序减法
                indexs.append(index - i)  # 找出排在前面n0个的Index
            for i in indexs:  # 判断index的大学，避免类似清华大学这种前面没有其他学校的情况出现
                if i >= 0:
                    outputSchool0.append(schoolName[i])
        except:
            pass
        try:
            indexs = []
            for i in range(1, n1 + 1):  # 正序加法
                indexs.append(index + i)  # 找出排在后面n1个的Index
            for i in indexs:  # 判断index的大学，避免类似最差学校这种后面没有其他学校的情况出现
                if i < len(schoolName):
                    outputSchool1.append(schoolName[i])
        except:
            pass

        #输出具体推荐的学校
        print('\n在',province,'，评分在 ' + inputSchool + ' 前面的学校：',end='')   #前面的学校
        if len(outputSchool0) == 0:   #证明为空列表
            print('无')
        else:
            for each in outputSchool0:
                print(each,' ',end='')

        print('\n在',province,'，评分在 ' + inputSchool + ' 后面的两个学校是： ',end='')  #后面的学校
        if len(outputSchool1) == 0:   #证明为空列表
            print('无')
        else:
            for each in outputSchool1:
                print(each,' ',end='')
    outputSchool = sum([outputSchool0, outputSchool1], [])
    return outputSchool


# # 1：用户端输入数据
# inputSchool = input("请输入你要查找的学校(如：佛山科学技术学院):")
# while inputSchool not in [x[0] for x in datasSorted ]:   #判断输入学校是否正确
#     inputSchool = input("输入学校不存在，请重新输入学校:")
#
# province = input('请输入要选择的省份，如：广东，北京，全国等（默认为上面学校的省份）：')
# while province not in [x[1] for x in datasSorted ]+['全国','']:  #判断输入省份是否正确
#     province = input("省份输入格式有误或省份不存在:")
#
# if province == '':  #如果不进行输入，默认为上面学校的省份
#     province = [data[1] for data in datasSorted if inputSchool == data[0]][0]
#
#
# # 2：主函数,参数为：输入的学校，输入的省份，全国各地学校的数据
# running(inputSchool,province,datasSorted)
