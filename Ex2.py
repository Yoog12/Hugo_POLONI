import pandas as pd
import numpy as np
data = pd.read_csv('mower_market_snapshot.csv', sep=';')
data.loc[data['product_type']=="essence","product_type"]=1
data.loc[data['product_type']=="auto-portee","product_type"]=2
data.loc[data['product_type']=="electrique","product_type"]=3
data.groupby('product_type').sum()
print(data)
