from django.shortcuts import render, redirect
from . import models
from user.models import User
import pandas as pd
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt    # 取消csrf


@csrf_exempt
def recommend_profession(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有信息一说，跳去登录界面
        return redirect("/login/")
    user = User.objects.get(username=request.session.get('username'))
    have_done = True
    if user.personality_type != '0':
        have_done = None
    title = '推荐专业'
    message = models.Profession.objects.values_list()
    s = models.Profession.objects.values('type1').distinct()

    message = pd.DataFrame(message)
    type1 = message.iloc[:, 1].unique()
    pro_js = serializers.serialize("json", models.Profession.objects.all())
    p_type = user.personality_type
    profession_hot1 = models.Profession.objects.filter(profession_type__contains=p_type[0])
    profession_hot2 = models.Profession.objects.filter(profession_type__contains=p_type[1])
    profession_hot3 = models.Profession.objects.filter(profession_type__contains=p_type[2])
    profession_hot = list(set(profession_hot1) | set(profession_hot1) | set(profession_hot1))
    profession_hot.sort()           # 排序
    profession_hot = profession_hot[: 20]   # 取前20个
    return render(request, 'recommend_profession.html', locals())


@csrf_exempt
def profession(request, profession_name):
    p = models.Profession.objects.get(profession_name=profession_name[: -2])
    p.profession_hot = int(p.profession_hot) + 1
    p.save()
    print(profession_name, '热度+1')
    return redirect(f'https://baike.baidu.com/item/{profession_name}')