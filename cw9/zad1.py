import pandas as pd
import numpy as np

df = pd.read_csv('imiona.csv')
print(df[ df['Liczba'] > 1000 ]) # - tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print(df[ df['Imię'] == 'GRZEGORZ' ]) # - tylko rekordy gdzie nadane imię jest takie jak Twoje
print(df.groupby(['Rok']).agg({'Liczba':['sum']})) # - sumę wszystkich urodzonych dzieci w całym danym okresie,

df2 = df[ (df['Rok'] >= 2000) & (df['Rok'] <= 2005) ]
print(df2['Liczba'].sum()) #- sumę dzieci urodzonych w latach 2000-2005

print(df.groupby(['Płeć']).agg({'Liczba':['sum']})) # - sumę urodzonych chłopców i dziewczynek,

grouped = df.loc[df.groupby(['Rok', 'Płeć'])["Liczba"].idxmax()] # - najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
print(grouped)

grouped2 = df.loc[df.groupby(['Płeć'])["Liczba"].idxmax()] # - najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
print(grouped2)