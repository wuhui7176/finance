# -*- coding:utf-8 -*-
"""

"""
import tushare as ts
import pandas as pd

import matplotlib.pyplot as plt

last = None

def t(x, y=None):
    # print x.name
    # print x
    last = x
    if x['close'] > x['ma5']:
        print u"突破5日线 %s %s %s" %(x.name, x['close'], x['ma5'])



"""
    向上突破5日线，到下跌突破5日线收益率
"""


def abc(code):
    """5日线"""
    p_data = ts.get_hist_data(code=code, start="2018-01-01")
    # p_data.apply(lambda x: t(x), axis=1)
    # p_data.set_index('date',  inplace=True)
    # p_data[u'5日'] = p_data['close'].rolling(5).mean()
    # p_data.loc[:, ['close', u'5日']].plot()
    # plt.show()

    # 查看突破5日线后, 最近5个交易日的上涨或下跌情况
    # axis = 1 按行 Series 传给 lambda 否则 按 列传
    #print p_data
    #print p_data['close']
    #print p_data.loc[:, ['close', u'5日']].rolling(3).apply(lambda x: t(x))
    #p_data['close', u'5日'].rolling(3).apply(lambda x: t(x))

    # new_data = p_data[['close', '5日']]

    # print new_data

abc('600295')
