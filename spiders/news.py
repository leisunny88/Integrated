import os

import requests
from bs4 import BeautifulSoup
import random
import time

# from django.conf import settings
# settings.configure()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')


class NewData(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        self.url = "https://www.hqck.net"
        self.time = random.randint(0, 2)
        self.url_list = []

    def get_news_link(self):
        html = requests.get(url=self.url, headers=self.headers)
        html.encoding = 'gb18030'  # 解决抓取后中文乱码的问题
        soup = BeautifulSoup(html.text, "lxml")
        div_list = soup.find_all('div', attrs={'class': 'content-item'})
        for li in div_list[1].find_all('li'):
            lt = []
            link = li.find('a').get('href')
            n_title = li.find('a').text
            tm = li.find('i', attrs={'class': 'fa fa-clock-o'})
            # print(self.url+link, n_title, tm.text)

            lt.append(tm.text)
            lk = self.url + link
            lt.append(lk)
            lt.append(n_title)
            self.url_list.append(lt)
            # NewsDataModel.objects.create(
            #     newstime=tm,
            #     newurl=self.url + link,
            #     title=n_title
            # )
            time.sleep(self.time)
        return self.url_list
