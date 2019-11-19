from django.urls import path, re_path
from . import views


urlpatterns = [
    path('school_info/', views.school_list, name='school_info'),
    path('school_info/<str:school_name>/', views.one_school, name='one_school'),
]