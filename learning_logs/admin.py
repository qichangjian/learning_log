from django.contrib import admin
from learning_logs.models import Topic,Entry

# Register your models here.

admin.site.register(Topic) #）让Django通过管理网站管理我们的模型

admin.site.register(Entry) #向管理网站注册Entry模型