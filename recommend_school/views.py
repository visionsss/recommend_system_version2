from django.shortcuts import render, redirect
from user.models import User
from . import models


def recommend_school(request):
    if not request.session.get('is_login', None):
        # 没登录去登录
        return redirect("/login/")
    title = '推荐学校'
    try:
        score = User.objects.filter(username=request.session['username'])[0].score
        if User.objects.filter(username=request.session['username'])[0].subject == 'art':
            student_type = '文科'
        else:
            student_type = '理科'
        print(score)
        for i in range(30, 600, 10):
            school = models.re_school.objects.filter(score_low__range=(score - i, score + i), student_type=student_type)
            if len(school) > 10:
                break
        print(school)
    except:
        pass
    return render(request, 'recommend_school.html', locals())