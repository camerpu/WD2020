import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('imiona.csv')
dzieci = df[df['Rok'] >= 2015].groupby(['Płeć']).agg({'Liczba':['sum']}) # - sumę wszystkich urodzonych dzieci w całym danym okresie,\
print(dzieci)
wykres = dzieci.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title('Liczba urodzeń dzieci')
plt.show()