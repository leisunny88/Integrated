#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: urls.py
@time: 2016/11/26 下午5:25
"""

from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = "oauth"
urlpatterns = [
    path(r'oauth/authorize', views.authorize),
    path(r'oauth/oauthlogin', views.oauthlogin, name='oauthlogin')
]
