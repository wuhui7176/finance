# -*- coding:utf-8 -*-
import tushare as ts
import time
import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# sz50 = ts.get_sz50s()

# sz50 = ts.get_hs300s()

sz50 = ts.get_zz500s()

codes = sz50['code']
# print codes


for s in codes:
    data = ts.get_hist_data(s, start="2018-10-11", end="2018-10-12")

    try:
        _data = data.loc['2018-10-11']
    except:
        continue

    # print _data
    # 放量并且下跌5个点
    if ((_data['volume'] - _data['v_ma5']) / _data['v_ma5']) >= 0.5 and _data['p_change'] <= -5:
        try:
            __data = data.loc['2018-10-12']
            print "fang", _data['p_change'],  s, __data['p_change']
        except:
            continue

    if ((_data['volume'] - _data['v_ma5']) / _data['v_ma5']) <= 0 and _data['p_change'] <= -5:
        try:
            __data = data.loc['2018-10-12']
            print "suo", _data['p_change'], s, __data['p_change']
        except:
            continue

    #
    # if ((_data['volume'] - _data['v_ma5']) / _data['v_ma5']) <=0 and _data['p_change'] > -5:
    #     __data = data.loc['2018-10-12']
    #     print s, __data['p_change']

    #
    # print "========================"
    #
    # if ((_data['volume'] - _data['v_ma5']) / _data['v_ma5']) <= 0:
    #     print s

    # time.sleep(10000)