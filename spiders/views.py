import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from spiders import models
from spiders.news import NewData, Video
import threading


def add_news(request):
    nd = NewData()
    url_list = nd.get_news_link()
    text_data_list = nd.news_text(2)
    for data in url_list:
        models.NewsDataModel.objects.create(
            newstime=data[0],
            newurl=data[1],
            title=data[2]
        )
    for data_list in text_data_list:
        models.NewsDataText.objects.create(
            name=data_list[0],
            text=data_list[1]
        )
    vd = Video()
    video_list = vd.get_video_link()
    for video_data in video_list:
        models.VideoModel.objects.create(
            playtime=video_data[0],
            title=video_data[1],
            link=video_data[2]
        )
    response = HttpResponse("添加成功")
    return response

