from django.shortcuts import render


def recommend_school(request):
    title = '推荐学校'
    return render(request, 'recommend_school.html', locals())