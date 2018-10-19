#!/usr/bin/env python
# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")

import tushare as ts
import pandas as pd
from mysql_test import execute_sql
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


def craw_industry():
    # 行业分类 type = 0 , 概念分类 type =2
    industry = ts.get_industry_classified()
    data = industry['c_name']
    data = data.drop_duplicates()
    for i in data:
        sql = "insert into plate(name, type) VALUE (%s, %s)"
        execute_sql(sql, [i, 0])


def creaw_concept():
    concept = ts.get_concept_classified()
    data = concept['c_name']
    data = data.drop_duplicates()
    print len(data)
    for i in data:
        sql = "insert into plate(name, type) VALUE (%s, %s)"
        execute_sql(sql, [i, 1])


def craw_stock():
    concept = ts.get_concept_classified()
    # print concept
    data = concept['name']
    # print len(data)
    data = data.drop_duplicates()
    print len(data)
    # for index, i in enumerate(data):
    #     c = concept.iloc[index]
    #     sql = "insert into stock(id, name) VALUE (%s, %s)"
    #     execute_sql(sql, [c['code'], i])


def test():
    s = pd.DataFrame([1, 2, 3])
    print s.iloc[0]


def all_stock():
    data = ts.get_stock_basics()
    data.to_csv("stock.csv")
    # for d in data.index:
    #     #print d, data.loc[d]
    #     sql = "insert into stock(id, name) VALUE (%s, %s)"
    #     execute_sql(sql, [d, data.loc[d]['name']])

# all_stock()


def stock():
    data = ts.get_stock_basics()
    for d in data.index:
        ts.get_hist_data(d)  # 一次性获取全部日k线数据


def test_group():
    # 分组

    _data = [[1, 2, 3], [4, 5, 3], [7, 8, 9]]
    data = pd.DataFrame(data=_data, columns=['a', 'b', 'c'])

    print data

    print "==========="
    s = data.groupby(by ='c').agg({'b': sum})
    print s


def csv_test():
    data = pd.read_csv("aaa.csv")
    data = data.sort_values(by='changepercent',axis = 0,ascending = False)
       # data = ts.get_today_all()
    #
    # data.to_csv("aaa.csv")
    print data
    pass


# csv_test()

def today():
  pass


# today()


# all_stock()
# test()

# craw_stock()


def merage_test():
    _data = [[1, 2, 3], [4, 5, 3], [7, 8, 9]]
    data1 = pd.DataFrame(data=_data, columns=['a', 'b', 'c'])

    # data1.where(data1> 1)
    _data2 = [[1, 2, 3], [6, 5, 3], [8, 8, 9]]
    data12 = pd.DataFrame(data=_data2, columns=['a', 'f', 'g'])

    s = pd.merge(left=data1, right=data12, on='a')


    print s


def concept_today():
    # concept = ts.get_concept_classified()
    # concept.to_csv("concept.csv")
    concept = pd.read_csv("concept.csv")
    data = pd.read_csv("aaa.csv")
    s = pd.merge(concept, data, left_on='code', right_on='code')
    s = s.groupby(by ='c_name').agg({'changepercent': sum})

    s = s.sort_values(by='changepercent',axis = 0,ascending = False)

    print s

# concept_today()


# merage_test()

