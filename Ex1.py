import pandas as pd
import numpy as np
data = pd.read_csv('mower_market_snapshot.csv', sep=';')
data['warranty']=data['warranty'].str[0]
data.groupby('warranty').sum()
print(data)
