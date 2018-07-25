#coding=UTF-8
from django.shortcuts import render

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'index.html')


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