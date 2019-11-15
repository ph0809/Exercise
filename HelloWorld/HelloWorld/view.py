# -*- coding: utf-8 -*-
# -*- author: ph -*-

'''这是视图文件'''
from django.http import HttpResponse
"""增加一个新的对象，用于向模板提交数据"""
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'   # context的键值对应hello.html中的元素
    return render(request, 'hello.html', context)    # render(request, template_name, context=None, content_type=None, status=None, using=None)

def index(request):
    return HttpResponse("good day!!")


def bio(request):
    return HttpResponse("nice girl!!!")


def weblog(request):
    return HttpResponse("welcome to my blog~~~")




