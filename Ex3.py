import pandas as pd
import numpy as np
data = pd.read_csv('mower_market_snapshot.csv', sep=';')
data['prod_cost'] = data.loc[:,'prod_cost']
# Remplace toute la colonne 'prod_cost' par des float et ignore "unknown"
data['prod_cost'] = pd.to_numeric(data['prod_cost'],errors='coerce')
# remplace toutes les valeurs inférieur ou égal à 0 par des NaN
data.loc[data['prod_cost'] <= 0 ] = np.nan
# Remplace tous les NaN par la moyenne des valeurs de la colonne 'prod_cost'
data['prod_cost'] = data['prod_cost'].fillna(data['prod_cost'].mean())
print(data)
