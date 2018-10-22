# -*- coding:utf-8 -*-

import tushare as ts
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# data = ts.get_h_data("600295")
#
# data.to_csv("600295")
# ts.get_hist_data("600295").to_csv("600295_")

data = pd.read_csv("600295_")

# print data
# data = data.reindex(index=data.index[::-1])

# 倒！！！
# for idx in reversed([1, 2, 4, 5]):
#     print idx


# print data
f = True
cs = 0
yl = 0
b_price = 0


for k in reversed(data.index):
    i =data.iloc[k]
    # print i
    if i['close'] > i['ma5'] and f:
        print "b", i['date'], i['ma5'], i['close']
        f = False
        cs += 1
        b_price = i['close']


    if i['close'] < i['ma5'] and not f:
        print "s", i['date'], i['ma5'], i['close']
        f = True
        cs += 1
        yl += (i['close'] - b_price) / b_price


print "交易次数", cs, yl




            # data = pd.read_csv("600295")
#
# print data

# plt.plot(data['date'],data['close'])
#
# plt.show()
