import pandas as pd
import numpy as np
tondeuse=pd.read_csv('mower_market_snapshot.csv',sep=';')
tondeuse2=tondeuse.loc[:,['id','attractiveness']]
tondeuse2[tondeuse2['attractiveness']>0.90]


tondeuse=pd.read_csv('mower_market_snapshot.csv',sep=';')
tondeuse3 = tondeuse.loc[:,['id','failure_rate']]
tondeuse3[tondeuse3['failure_rate']>0.04]


tondeuse=pd.read_csv('mower_market_snapshot.csv',sep=';')
tondeuse4 = tondeuse.loc[:,['id','failure_rate']]
tondeuse4.sort_values(by='id', ascending=False).head()

df=pd.read_csv('mower_market_snapshot.csv',sep=';')
df2 = tondeuse.loc[:,['capacity','id','failure_rate','warranty']]
df2=df2.copy()
df2.drop_duplicates()


df=pd.read_csv('mower_market_snapshot.csv',sep=';')
df2 = pd.DataFrame({'quality': ['low'], 'product_type': ['auto-portee']})
df3 = pd.DataFrame({'id': [18268,18943,19275]})
pd.concat([df2,df3])


df=pd.read_csv('mower_market_snapshot.csv',sep=';')
df2 = pd.DataFrame({'quality': ['Low'],'id': ['18268']})
df3 = pd.DataFrame({'id': ['18268']})
pd.concat([df2,df3])

df2 = pd.DataFrame({'quality': ['Low'],'id': ['18268']})
df3 = pd.DataFrame({'id': ['19307']})
pd.concat([df2, df3], join = 'inner')

df=pd.read_csv('mower_market_snapshot.csv',sep=';')
df2.groupby('quality').sum()

df=pd.read_csv('mower_market_snapshot.csv',sep=';')
df6=df.loc[:,['warranty','product_type','prod_cost']]
print(df6)

df=pd.read_csv('mower_market_snapshot.csv',sep=';')
df8=df.iloc[:650] # affichage des 650 premières lignes
df9=df.iloc[650:] # affichage des 650 dernières lignes
print(df8)
print(df9)
