#coding=UTF-8
"""定义learning_logs的URL模式"""
from django.urls.conf import path

from . import views


#app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index,name='index'),
    
]