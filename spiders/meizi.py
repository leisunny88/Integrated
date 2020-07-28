import time

import requests
from bs4 import BeautifulSoup
import random
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.DEFAULT_RETRIES = 5
"""
为项目抓取静态资源
"""


class MeiZi(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            'Connection': 'close'
        }
        self.url = "http://www.mzitu.com/all"
        self.url_list = []
        self.time = random.randint(0, 3)

    def get_data_all(self):

        data_list = requests.get(url=self.url, headers=self.headers)
        soup = BeautifulSoup(data_list.text, "lxml")
        ul_list = soup.find_all("ul", attrs={"class": "archives"})
        li_list = ul_list[0].find_all("li")
        for li in li_list:
            for p in li.find_all("p", attrs={"class": "url"}):
                # print(p.find_all("a"))
                for a in p.find_all("a"):
                    url = re.search(".*href=(.*).*target=(.*)", str(a))
                    self.url_list.append(url.group(1))
                    time.sleep(self.time)
                    s = requests.session()
                    s.keep_alive = False
        print(len(self.url_list))

    def get_image(self):

        i = 1
        try:
            for url in self.url_list:
                try:
                    n_url = url.split('"')[1] + "/%s" % str(i)
                    print(n_url)
                    h_html = requests.get(url=n_url, headers=self.headers, timeout=30, verify=False)
                    h_soup = BeautifulSoup(h_html.text, "lxml")
                    p_lt = h_soup.find_all("div", attrs={"class": "main-image"})
                    time.sleep(self.time)
                    print(p_lt)
                    i += 1
                    s = requests.session()
                    s.keep_alive = False
                except Exception as ex:
                    i = 1
        except requests.exceptions.ConnectionError:
            print('Handle Exception')


mz = MeiZi()
mz.get_data_all()
# mz.get_image()
