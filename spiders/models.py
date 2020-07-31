from django.db import models


# Create your models here.
class MeiZiTu(models.Model):
    tutime = models.CharField(max_length=30)
    imgname = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=150)


class NewsDataModel(models.Model):
    newstime = models.CharField(max_length=30)
    newurl = models.CharField(max_length=100)
    title = models.CharField(max_length=100)


class ANovelModel(models.Model):
    antime = models.CharField(max_length=30)
    name = models.CharField(max_length=100, null=None)
    link = models.CharField(max_length=100, null=None)


class VideoModel(models.Model):
    playtime = models.CharField(max_length=30, null=None)
    title = models.CharField(max_length=100, null=None)
    link = models.CharField(max_length=100, null=None)
