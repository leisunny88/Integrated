from django.db import models


# Create your models here.
class MeiZiTu(models.Model):
    id = models.AutoField(primary_key=True)
    tutime = models.CharField(max_length=30)
    imgname = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    img = models.CharField(max_length=150)


class NewsDataModel(models.Model):
    id = models.AutoField(primary_key=True)
    newstime = models.CharField(max_length=30)
    newurl = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    detail = models.OneToOneField('NewsDataText', on_delete=models.CASCADE)


class NewsDataText(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        db_table = "news_text"


class ANovelModel(models.Model):
    id = models.AutoField(primary_key=True)
    antime = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    detail = models.OneToOneField('ANovelDataText', on_delete=models.CASCADE)

    class Meta:
        db_table = "anovel"


class ANovelDataText(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        db_table = "anovel_text"


class VideoModel(models.Model):
    id = models.AutoField(primary_key=True)
    playtime = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    class Meta:
        db_table = "video"
