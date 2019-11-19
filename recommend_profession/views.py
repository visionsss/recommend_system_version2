from django.shortcuts import render
from . import models
import pandas as pd
from django.core import serializers


def recommend_profession(request):
    title = '推荐专业'
    return render(request, 'recommend_profession.html', locals())
