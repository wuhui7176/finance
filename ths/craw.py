#!/usr/bin/env python
# encoding: utf-8
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd

reload(sys)
sys.setdefaultencoding("utf8")

def craw():
    h =  {
        "User-Agent":    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36"
    }
    content = requests.get("http://q.10jqka.com.cn/gn/", headers=h).content

    ths = BeautifulSoup(content, "lxml")

    items = ths.select(".cate_items")

    data = pd.DataFrame(columns=[u'链接', u'名称'])

    for item in items:
        a = item.select("a")
        for i in a:
            data = data.append({u"链接": i['href'], u"名称": i.text}, ignore_index=True)
            print i['href'], i.text
    data.to_csv(u"概念板块.csv")



craw()
#
# data = pd.DataFrame(columns=[u'链接', u'名称'])
# data = data.append({u"链接": '111', u"名称": '222'}, ignore_index=True)
# data.to_csv(u"概念板块.csv")





