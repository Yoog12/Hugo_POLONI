import pandas as pd
import numpy as np
data = pd.read_csv('mower_market_snapshot.csv', sep=';')
data = pd.DataFrame(np.array(data).reshape(1399,11),columns = list ( 'ABCDEFGHIJK' ))

print(data)