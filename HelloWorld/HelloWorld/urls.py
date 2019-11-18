"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.conf.urls import url
from . import view

# urlpatterns = [
#     url(r'^$', view.hello),    # 这是视图文件里的方法, 第一个参数是一个正则表达式
#                                  # ^:匹配输入字符串的开始位置,$:匹配输入字符串的结尾位置
#
#     # url('hello/', view.hello),  # 前一个参数表示输入网址时端口后面的路径，后一个参数表示view中hello方法的内容。 若果有两个url,则会覆盖上一个
#
# ]


"""Django2.0中可以使用re_path()方法来兼容1.x版本中的url()方法，一些正则表达式的规则也可以通过re_path()来实现"""
# from django.urls import include, re_path
#
# urlpatterns = [
#     re_path(r'^index/$', view.index, name='index'),    # re_path相当于路由分发
#     re_path(r'^bio/(?P<username>\w+)/$', view.bio, name='bio'),
#     # re_path(r'^weblog/', include('blog.urls')),
# ]


"""Django >= 2.0的版本， django.conf.urls====>django.urls取代"""
# from django.urls import path
# from . import view
#
# urlpatterns = [
#     path('hello/', view.hello),
#     # path('world/', view.world),   # 如果是路径，后面必须加/
# ]

# from django.conf.urls import *
# from . import view, testdb
#
# urlpatterns = [
#     url(r'^hello$', view.hello),
#     url(r'^testdb$', testdb.testdb),
#     url(r'^search_form$', search.search_form),
#     url(r'^search$', search.search),
#     url(r'^search-post$', search2.search_post),
# ]

