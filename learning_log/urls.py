"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import  include
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path


urlpatterns = [ #����urlpatterns������Ŀ�е�Ӧ�ó����URL
    path('admin/', admin.site.urls), #���Ĵ������ģ��admin.site.urls����ģ�鶨���˿��ڹ�����վ�����������URL��
    re_path('', include('learning_logs.urls')),
    re_path('users/',include('users.urls'))

#     path('index',learn_view.index),
#     path('index1/',learn_view.index1),
#     path('add/', learn_view.add,name='add'),
#     path('add2/<int:a>/<int:b>', learn_view.add2,name='add2'),

]
