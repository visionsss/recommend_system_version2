from django.urls import path, re_path
from . import views


urlpatterns = [
    path('recommend_profession',
         views.recommend_profession, name='recommend_profession'),
]