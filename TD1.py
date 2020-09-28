import pandas as pd
import numpy as np
data = pd.read_csv('mower_market_snapshot.csv', sep=';', index_col=0)

print(data)