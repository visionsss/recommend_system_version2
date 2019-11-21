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
    title = '推荐专业'
    message = models.Profession.objects.values_list()
    s = models.Profession.objects.values('type1').distinct()

    message = pd.DataFrame(message)
    type1 = message.iloc[:, 1].unique()
    pro_js = serializers.serialize("json", models.Profession.objects.all())
    profession_hot = models.Profession_Hot.objects.filter().order_by('id')[:10]
    return render(request, 'recommend_profession.html', locals())
