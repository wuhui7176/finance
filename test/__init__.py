#
import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pass

import tushare as ts

# print ts.get_k_data("600285")

data = ts.get_hist_data("600295")
print data

# print data[data["volume"] <= 30000]