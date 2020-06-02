import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('imiona.csv')
dzieci = df.groupby(['Płeć']).agg({'Liczba':['sum']}) # - sumę wszystkich urodzonych dzieci w całym danym okresie,\
print(dzieci)
wykres = dzieci.plot.bar()
wykres.set_ylabel('Liczb urodzin')
wykres.set_xlabel('Płeć')
wykres.legend()
plt.title('Liczba urodzeń z podziałem na płeć')
plt.show()