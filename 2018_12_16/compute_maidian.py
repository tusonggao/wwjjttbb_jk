import pandas as pd
from datetime import datetime

now = datetime.now()
print(now.year, now.month, now.day)

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
print(delta)

df = pd.read_csv('df_maidian_small.csv', index_col=0)
print('df.columns is ', df.columns)

df2 = pd.pivot_table(df, index=['date'])
print(df2.shape)