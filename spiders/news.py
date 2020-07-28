import requests
from bs4 import BeautifulSoup
import random
import time

class NewData(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        self.url = "https://www.hqck.net"
        self.time = random.randint(1, 3)


    def get_news_link(self):
        html = requests.get(url=self.url, headers=self.headers)
        html.encoding = 'gb18030'  # 解决抓取后中文乱码的问题
        soup = BeautifulSoup(html.text, "lxml")
        div_list = soup.find_all('div', attrs={'class':'content-item'})
        for li in div_list[1].find_all('li'):
            link = li.find('a').get('href')
            title = li.find('a').text
            tm = li.find('i', attrs={'class':'fa fa-clock-o'})
            print(self.url+link, title, tm.text)
            time.sleep(self.time)



nd = NewData()
nd.get_news_link()