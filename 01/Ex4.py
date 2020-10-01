#Custom functions

def Treatment_1(name): #Fonction d'import du CSV
    global ID
    df = pd.read_csv(name, sep=";", header=None) #df = dataframe de notre CSV sans en-tête
    df.columns = df.iloc[0, :].tolist() # df.columns = Sélection de toutes les colones et ajout dans une liste
    df = df.drop(0, axis = 0).reset_index(drop = True)# Drop de tous les index puis suppression d'une evntuel colones index
    ID = df.id #
    df = df.drop('id', axis =  1)
    return df

def Treatment_2(df):
    lb_make = LabelEncoder()      #Let's transform our string categorical data to numeric categorical data !
    label_list = df.columns[5:7].tolist() #label_list = liste les colones 5 à 7
    wa = df.columns[7] #wa = colonnes 7
    numeric_list = df.columns[~df.columns.isin(df.columns[5:8])].tolist() #numeric_list = liste de colonne qui ne sont pas dans les colonnes 5 à 8
    for x in df.columns: # pour x dans df colonne
        for w in df.index: #pour w dans df index
            if x in numeric_list: #Si x dans numeric_list
                if df[x][w] == 'unknown': #Si les valeurs index et colonnes sont nuls
                    df[x][w] = 0 #Ces valeurs sont misent à 0
            elif x in wa:
                df[x][w] = df[x][w][0]
            elif x in label_list:
                df[str(x)+'_encoded'] = lb_make.fit_transform(df[x]) #Crée 2 nouvelles liste avec un suffixe '_encoded' et rempli avec les valeurs des colonnes par des 0, des 1 et des 2
    if 'market_share' in df.columns.tolist():
        df = df.drop('market_share', axis = 1)#Colonne "market_share" retirée
    df = df.drop(label_list, axis = 1)#Colonne "label_list" retirée
    for x in df.columns:
        df[x] = df[x].astype(float)#Conversion des donner en float
    return df

    return df

#Improve this treatment :)
def Treatment_3(df):
    import math
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import OneHotEncoder
    df.loc[df['prod_cost'] <= 0, 'prod_cost'] = np.nan #Remplacement des 0 et des nombres négatifs par des NaN
    for x, y in zip(df.prod_cost, df.index):
        rep = math.isnan(df.prod_cost[y]) #rep = toutes les valeurs NaN
        if rep == True or x == 0 or x < 0:
            df['prod_cost'][y] = df['prod_cost'].mean() #moyenne des données "prod_cost"
    return df

#Files
name_1 = 'mower_market_snapshot.csv'
