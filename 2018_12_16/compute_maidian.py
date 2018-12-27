import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# now = datetime.now()
# print(now.year, now.month, now.day)

# delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
# print(delta)

# df = pd.read_csv('df_maidian_small.csv', index_col=0)
# print('df.columns is ', df.columns)

# df2 = pd.pivot_table(df, index=['date'])
# print(df2.head(5))

# df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
#                    "bar", "bar", "bar", "bar"],
#                    "B": ["one", "one", "one", "two", "two",
#                          "one", "one", "two", "two"],
#                    "C": ["small", "large", "large", "small",
#                          "small", "large", "small", "small",
#                          "large"],
#                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7]})

# table = pd.pivot_table(df, values='D', index=['A', 'B'],
#                        columns=['C'], aggfunc=np.sum)
# print('table is ', table)


df = pd.read_csv('F:/linux_folder/tsg/hive_sql_4_output', sep='\t')
print(df.shape, df.head())


df.value.plot()
plt.show()

