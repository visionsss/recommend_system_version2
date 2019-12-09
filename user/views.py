from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt    # 取消csrf
from . import forms
from . import models
# Create your views here.


@csrf_exempt
def index(request):
    title = '首页'
    return render(request, 'index.html', locals())


@csrf_exempt
def login(request):
    title = '登录'
    error = ''
    login_form = forms.LoginForm()
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():  # 判断是否填写完成
            user = login_form.cleaned_data  # 清理数据
            user_info = models.User.objects.get(username=user['username'])
            request.session['is_login'] = True
            request.session['username'] = user['username']
            request.session['school_name'] = ''
            request.session['province'] = ''
            request.session['student_type'] = user_info.subject
            request.session['epoch'] = '本科批'
            return redirect('/')
        else:
            # 获取全局的error信息,只显示第一个
            if login_form.errors.get('__all__'):
                error = login_form.errors.get('__all__')[0]

    return render(request, 'login.html', locals())


@csrf_exempt
def register(request):
    title = '注册'
    error = ''
    register_form = forms.RegisterForm()
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():    # 判断是否填写完成
            user = register_form.cleaned_data  # 清理数据
            models.User.objects.create(username=user['username'], password=user['password1'])
            return redirect('/login/')
        else:
            # 获取全局的error信息,只显示第一个
            if register_form.errors.get('__all__'):
                error = register_form.errors.get('__all__')[0]

    return render(request, 'register.html', locals())


@csrf_exempt
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush()
    return redirect("/")


@csrf_exempt
def student_info(request):
    title = '个人信息'
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有信息一说，跳去登录界面
        return redirect("/login/")
    username = request.session.get('username', None)
    user = models.User.objects.get(username=username)
    if request.method == 'GET':
        student_form = forms.StudentInfoForm(initial={
            'sex': user.sex,
            'province': user.province,
            'subject': user.subject,
            'score': user.score,
        })
    if request.method == 'POST':
        student_form = forms.StudentInfoForm(request.POST)
        if student_form.is_valid():  # 判断是否填写完成
            user.sex = student_form.cleaned_data['sex']
            user.province = student_form.cleaned_data['province']
            user.subject = student_form.cleaned_data['subject']
            user.score = student_form.cleaned_data['score']
            user.save()
            message = '修改成功'
            request.session['student_type'] = student_form.cleaned_data['subject']
    return render(request, 'student_info.html', locals())
