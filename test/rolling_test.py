import numpy as np
import pandas as pd

data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

df = pd.DataFrame(data=data, index=['a', 'b', 'c', 'd'], columns=['d', 'e', 'f'])

# print df


def abc(x):
    print x
    return x.mean()


print df.rolling(2).apply(lambda x: abc(x))


print "123"