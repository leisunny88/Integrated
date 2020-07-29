from django.shortcuts import render

# Create your views here.
from spiders.models import NewsDataModel


def index(request):
    all_news = NewsDataModel.objects.all()
    return render(request, 'index.html', {'news_list':all_news})


def newspage(request):
    all_news = NewsDataModel.objects.all()

    return render(request, './anovel.html', {'news_list':all_news})