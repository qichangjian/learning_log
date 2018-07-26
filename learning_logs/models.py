#coding=UTF-8
from django.contrib.auth.models import User
from django.db import models


# Create your models here.定义模型
class Topic(models.Model):   #创建了一个名为Topic的类，它继承了Model——Django中一个定义了模型基本功能的类。
    """用户学习的"""
    text = models.CharField(max_length=200) #属性text是一个CharField——由字符或文本组成的数据
    date_added = models.DateTimeField(auto_now_add=True) #属性date_added是一个DateTimeField——记录日期和时间的数据
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self): #我们需要告诉Django，默认应使用哪个属性来显示有关主题的信息。Django调用方法__str__()来显示模型的简单表示
        """返回模型的字符串表示"""
        return self.text
    
class Entry(models.Model):
    """学到的有关某个主题的具体指示"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) #第一个属性topic是一个ForeignKey实例（见）。外键是一个数据库术语，它引用了数据库中的另一条记录
    text = models.TextField() #是属性text，它是一个TextField实例（见）。这种字段不需要长度限制   
    date_added = models.DateTimeField(auto_now_add=True) #属性date_added让我们能够按创建顺序呈现条目，并在每个条目旁边放置时间戳。
    
    class Meta: #在Entry类中嵌套了Meta类。Meta存储用于管理模型的额外信息，在这里，它让我们能够设置一个特殊属性，让Django在需要时使用Entries来表示多个条目
        verbose_name_plural = 'entries'
        
    def __str__(self): #方法__str__()告诉Django，呈现条目时应显示哪些信息。由于条目包含的文本可能很长，我们让Django只显示text的前50个字符（见）。我们还添加了一个省略号，指出显示的并非整个条目
        """返回模型的字符串表示"""
        return self.text[0:50] + "..."
    