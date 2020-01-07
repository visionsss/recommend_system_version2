from django.shortcuts import render, redirect
from user.models import User
from . import models
from . import forms


def recommend_school(request):
    if not request.session.get('is_login', None):
        # 没登录去登录
        return redirect("/login/")
    title = '推荐学校'
    if request.method == 'POST':
        request.session['school_name'] = request.POST.get('school_name')
        request.session['province'] = request.POST.get('province')
        # request.session['student_type'] = request.POST.get('student_type')
        request.session['epoch'] = request.POST.get('epoch')
    user = User.objects.get(username=request.session['username'])
    score = user.score - 10
    for i in range(30, 600, 10):
        schools = models.School_info.objects.filter(
            school_name__contains=request.session['school_name'],
            student_type__contains=request.session['student_type'],
            epoch__contains=request.session['epoch'],
            school_province__contains=request.session['province'],
            lowest_score__range=(score - i, score + i), student_type=user.subject)
        if len(schools) > 12:
            break
    schools = sorted(schools)[len(schools)//2-5: len(schools)//2+5]
    school_form = forms.school_form(initial={
        'school_name': request.session['school_name'], 'province': request.session['province'],
        'student_type': request.session['student_type'], 'epoch': request.session['epoch']
    })
    school_form.student_type = None
    return render(request, 'recommend_school.html', locals())
