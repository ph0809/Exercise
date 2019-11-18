# -*- coding: utf-8 -*-
# -*- author: ph -*-

from django.shortcuts import render
from django.views.decorators import csrf

def searcH_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)