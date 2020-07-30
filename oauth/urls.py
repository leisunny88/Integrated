#!/usr/bin/env python
# encoding: utf-8


from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name = "oauth"
urlpatterns = [
    path(r'oauth/authorize', views.authorize),
    path(r'oauth/oauthlogin', views.oauthlogin, name='oauthlogin')
]
