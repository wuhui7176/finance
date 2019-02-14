#!/usr/bin/env python
# encoding: utf-8
import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import traceback

reload(sys)
sys.setdefaultencoding("utf8")
h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3534.4 Safari/537.36",
    "cookie": "searchGuide=sg; __utma=156575163.591409901.1536905447.1540966141.1541144919.3; __utmz=156575163.1541144919.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1548906532,1548913844,1548913858,1548913860; historystock=000636; spversion=20130314; v=Au_bjTXp7wSkxes4gWBhb24Jfgj6lEIW3e5HqgF_iTpnegX-CWTTBu241_cS"
}

def craw():
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


def craw2():
    r_data = pd.DataFrame(columns=[u'板块名称', u'名称', u'代码'])

    try:
        data = pd.read_csv(u"概念板块.csv")
        for index, _ in enumerate(data.values):
            ths_data = data.iloc[index]
            craw_url = ths_data[u'链接']
            h_code = craw_url[-7: -1]
            content = requests.get(craw_url, headers=h).content
            ths = BeautifulSoup(content, "lxml")
            field = ths.select_one(".desc")['field']
            maincont = ths.select_one("#maincont")
            tr = maincont.select("tr")
            for index,t in enumerate(tr):
                if index == 0 :
                    continue
                tds = t.select("td")
                code = tds[1].text
                name = tds[2].text
                print ths_data[u'名称'], code, name
                r_data = r_data.append({u"板块名称": ths_data[u'名称'], u"名称": name, u'代码': code}, ignore_index=True)

            try:
                page_info = ths.select_one(".page_info").text
            except Exception as e:
                traceback.print_exc(e)
                continue
            page_totle = page_info.split("/")[1]

            if int(page_totle) > 1:
                for i in range(2, int(page_totle)):
                    craw_url = "http://q.10jqka.com.cn/gn/detail/field/{}/order/desc/page/{}/ajax/1/code/{}".format(field,
                                                                                                                    str(i),
                                                                                                                    h_code)
                    content = requests.get(craw_url, headers=h).content
                    ths = BeautifulSoup(content, "lxml")
                    tr = ths.select("tr")
                    for index, t in enumerate(tr):
                        if index == 0:
                            continue
                        tds = t.select("td")
                        code = tds[1].text
                        name = tds[2].text
                        print ths_data[u'名称'], code, name
                        r_data = r_data.append({u"板块名称": ths_data[u'名称'], u"名称": name, u'代码': code}, ignore_index=True)

    except Exception as e:
        traceback.print_exc(e)

    r_data.to_csv(u"代码.csv")

craw2()

# s = "http://q.10jqka.com.cn/gn/detail/code/301558/"
# print s[-7: -1]

#
# data = pd.DataFrame(columns=[u'链接', u'名称'])
# data = data.append({u"链接": '111', u"名称": '222'}, ignore_index=True)
# data.to_csv(u"概念板块.csv")





