#coding=UTF-8
"""定义learning_logs的URL模式"""
from django.urls.conf import path

from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    path('', views.index,name='index'),
    
    path('topics/',views.topics,name='topics'),
    
    path('topics/<int:topic_id>',views.topic,name='topic'),
    
    path('new_topic',views.new_topic,name='new_topic'),
    
    #用于添加新条目的页面
    path('new_entry/<int:topic_id>',views.new_entry,name="new_entry"),
    
    #编辑条目
    path('edit_entry/<int:entry_id>',views.edit_entry,name='edit_entry'),
    
]