from django.db import models

# Create your models here.
class MeiZiTu(models.Model):
    pass


class NewsDataModel(models.Model):
    newstime = models.CharField(max_length=30)
    newurl = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
