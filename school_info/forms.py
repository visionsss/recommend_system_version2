from django import forms


class school_form(forms.Form):
    province_gender = (
        ('', "全部"),
        ('广东', "广东"),
        ('安徽', "安徽"),
        ('澳门', "澳门"),
        ('北京市', "北京市"),
        ('福建', "福建"),
        ('甘肃', "甘肃"),
        ('广西', "广西"),
        ('贵州', "贵州"),
        ('海南', "海南"),
        ('河北', "河北"),
        ('河南', "河南"),
        ('黑龙江', "黑龙江"),
        ('湖北', "湖北"),
        ('湖南', "湖南"),
        ('吉林', "吉林"),
        ('江苏', "江苏"),
        ('辽宁', "辽宁"),
        ('马来西亚', "马来西亚"),
        ('内蒙古', "内蒙古"),
        ('宁夏', "宁夏"),
        ('青海', "青海"),
        ('山东', "山东"),
        ('山西', "山西"),
        ('陕西', "陕西"),
        ('上海市', "上海市"),
        ('四川', "四川"),
        ('天津市', "天津市"),
        ('西藏', "西藏"),
        ('香港', "香港"),
        ('新疆', "新疆"),
        ('云南', "云南"),
        ('浙江', "浙江"),
        ('重庆市', "重庆市"),
    )
    student_gender = (
        ('理科', '理科'),
        ('文科', '文科'),
    )
    epoch_gender = (
        ('本科批', '本科批'),
        ('专科批', '专科批'),
        ('本科提前批', '本科提前批'),
    )
    school_name = forms.CharField(label="院校名称", empty_value='')
    province = forms.ChoiceField(label='省份', choices=province_gender)
    student_type = forms.ChoiceField(label='考生类别', choices=student_gender)
    epoch = forms.ChoiceField(label='录取批次', choices=epoch_gender)


class one_school_form(forms.Form):
    profession_name = forms.CharField(label="专业名称", empty_value='')
    year = forms.ChoiceField(label='年份', choices=((2014, 2014), (2015, 2015),))
    epoch = forms.ChoiceField(label='录取批次')
