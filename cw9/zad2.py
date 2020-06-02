import pandas as pd
import numpy as np
df = pd.read_csv('zamowienia.csv', sep=';')

#df_dropped = df.drop_duplicates(subset=['Sprzedawca'])
#print(df_dropped['Sprzedawca'])

#df_sorted = df.sort_values('Utarg')
#print(df_sorted[-5:])

#print(df.groupby(['Sprzedawca']).size())

#print(df.groupby(['Kraj']).agg({'Utarg':['sum']}))

#print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'].str.contains("2005"))].groupby(['Kraj']).agg({'Utarg':['sum']}))

print(df[(df['Data zamowienia'].str.contains("2004"))].agg({'Utarg':['mean']}))

df[(df['Data zamowienia'].str.contains("2005"))].to_csv('2005.csv')
df[(df['Data zamowienia'].str.contains("2004"))].to_csv('2004.csv')
