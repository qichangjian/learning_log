#coding=UTF-8
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls.base import reverse

from learning_logs.forms import TopicForm, EntryForm
from learning_logs.models import Topic, Entry
from django.db.transaction import commit


# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'index.html')

@login_required
def topics(request):#函数topics()包含一个形参：Django从服务器那里收到的request对象
    """显示所有的主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') #数据库中获取owner属性为当前用户的Topic对象
    #topics = Topic.objects.order_by('date_added')#，我们查询数据库——请求提供Topic对象，并按属性date_added对它们进行排序。我们将返回的查询集存储在topics
    context = {'topics':topics} #我们定义了一个将要发送给模板的上下文。上下文是一个字典，其中的键是我们将在模板中用来访问数据的名称，而值是我们要发送给模板的数据。在这里，只有一个键—值对，它包含我们将在网页中显示的一组主题
    return render(request,'topics.html',context)

@login_required
def topic(request,topic_id):
    """显示单个主题以及所有的条目"""
    topic = Topic.objects.get(id=topic_id) #我们使用get()来获取指定的主题
    #确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404  #服务器上没有请求的资源时，标准的做法是返回404响应。在这里，我们导入了异常Http404（见），并在用户请求它不能查看的主题时引发这个异
    entries = topic.entry_set.order_by('-date_added') #我们获取与该主题相关联的条目，并将它们按date_added排序：date_added前面的减号指定按降序排列，即先显示最近的条目
    context = {'topic':topic,'entries':entries} #将主题和条目都存储在字典context中
    return render(request, 'topic.html',context) #再将这个字典发送给模板topic.html

@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        #未提交数据： 创建一个新的表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False) #调用form.save()，并传递实参commit=False，这是因为我们先修改新主题，再将其保存到数据库中
            new_topic.owner = request.user #将新主题的owner属性设置为当前用户
            new_topic.save() #在主题包含所有必不可少的数据，将被成功地保存。
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    
    context = {'form':form}
    return render(request,'new_topic.html',context)

@login_required 
def new_entry(request,topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        #未提交数据，创建一个空表单
        form = EntryForm()
    else:
        #post提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            """调用save()时，我们传递了实参commit=False（见.），让Django创建一个新的条目对象，并将其存储到new_entry中，但不将它保存到数据库中。我们将new_entry的属性topic设置为在这个函数开头从数据库中获取的主题"""
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save() #且不指定任何实参。这将把条目保存到数据库，并将其与正确的主题相关联。
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    
    context = {'topic':topic,'form':form}
    return render(request,'new_entry.html',context)    

@login_required
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        #初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST) #处理POST请求时，我们传递实参instance=entry和data=request.POST（见.），让Django根据既有条目对象创建一个表单实例，并根据request.POST中的相关数据对其进行修
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
        
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request, 'edit_entry.html',context) 
    






'''
from django.http import HttpResponse
def index1(request):
    return HttpResponse(u"欢迎光临 自强学堂!")


from django.shortcuts import render
from django.http import HttpResponse
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
'''