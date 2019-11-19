from django.shortcuts import render, redirect
from user import models
from . import models as t_model


def test(request, num, answer):
    num = int(num)
    try:
        question = t_model.Question.objects.get(pk=int(num))
    except:
        user = models.User.objects.get(username=request.session.get('username'))
        p_type = 'user.personality_type'
        user.personality_type = '人格类型1'
        user.save()
        return redirect('/analysis')
    num = num + 1
    answer_yes = answer + '1'
    answer_no = answer + '0'
    if num < 10:
        if num == 1:
            answer = '*'
        num = '0' + str(num)
    else:
        num = str(num)
    return render(request, 'test.html', locals())


def analysis(request):
    title = '性格分析'
    # 没登录的跳去登录界面
    if request.session.get('is_login', None) is None:
        return redirect('/login')
    user = models.User.objects.get(username=request.session.get('username'))
    content = '分析的内容'
    p_type = user.personality_type
    if p_type == '0':
        return redirect('/test/01/*/')
    return render(request, 'analysis.html', locals())
