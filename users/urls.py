#coding=UTF-8
"""定义users的URL模式"""
from django.contrib.auth.views import login
from django.urls.conf import path

from users import views


app_name = 'users'
urlpatterns = [
    # login page.
    path('login/',login,{'template_name': 'login.html'},name='login'),
    
    #login out page
    path('logout/',views.logout_view,name='logout'),
    
    #register
    path('register/',views.register,name='register')
]