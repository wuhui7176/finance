

import pandas as pd


pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = pd.read_excel("r.xls")

print type(data)
