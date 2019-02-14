#!/usr/bin/env python
# encoding: utf-8
import sys
import requests
import pandas as pd
import datetime
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf8")

headers = {
    "cookie": "searchGuide=sg; __utma=156575163.591409901.1536905447.1540966141.1541144919.3; __utmz=156575163.1541144919.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); spversion=20130314; historystock=300659%7C*%7C000636; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1550037854,1550038457,1550038462,1550038603; v=Atvv0enNAwFkP391eIS969pVajRGsO5I6cWzKM0YsW_wkPEiVYB_AvmUQ2ze",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3534.4 Safari/537.36"
}


def craw():
    start_url = ["http://q.10jqka.com.cn/thshy/index/field/199112/order/desc/page/1/ajax/1/",
                 "http://q.10jqka.com.cn/thshy/index/field/199112/order/desc/page/2/ajax/1/"]
    for index, url in enumerate(start_url):
        content = requests.get(url,
                               headers=headers).content
        content = content.decode("GBK").encode("utf-8")
        data = pd.read_html(content, encoding="utf-8")
        # data_frame = pd.concat(data)

        df = data[0]
        print df
        df.to_csv("{}industry_{}.csv".format(datetime.datetime.now().strftime('%Y-%m-%d'), index))
    #

def craw2():
    index = 10
    d = pd.DataFrame()
    try:
        for i in range(index):
            content = requests.get("http://q.10jqka.com.cn/index/index/board/all/field/zdf/order/desc/page/{}/ajax/1/".format(i),
                         headers=headers).content

            content = content.decode("GBK").encode("utf-8")
            data = pd.read_html(content, encoding="utf-8")
            if d.empty:
                d = data[0]
            else:
                d = pd.merge(d, data[0], how="outer")
    except:
        pass



    d.to_csv("2")

# craw2()

craw()

# p1 = pd.read_csv("2019-02-13industry_0.csv")
# p2 = pd.read_csv("2019-02-13industry_1.csv")
#
# p3 = pd.merge(p1, p2, how="outer")
# print p3
# pd.DataFrame().reset_index()
# p3.reset_index(u"Unnamed: 0")
# p3 = pd.concat(p1, p2)

# print p3
