import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from spiders import models
from spiders.news import NewData


def add_news(request):
    nd = NewData()
    url_list = nd.get_news_link()
    for data in url_list:
        print(data)
        models.NewsDataModel.objects.create(
            newstime=data[0],
            newurl=data[1],
            title=data[2]
        )
    response = HttpResponse("添加成功")
    return response

