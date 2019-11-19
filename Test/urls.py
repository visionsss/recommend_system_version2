from django.urls import path, re_path
from . import views


urlpatterns = [
    path('analysis/', views.analysis, name='analysis'),
    path('test/<int:num>/<str:answer>/', views.test, name='test'),
]