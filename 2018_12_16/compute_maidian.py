import pandas as pd
from datetime import datetime

now = datetime.now()
print(now.year, now.month, now.day)

df = pd.read_csv('df_maidian_small.csv')
print(df.shape)