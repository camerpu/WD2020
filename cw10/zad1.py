import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('imiona.csv')
dzieci = df.groupby(['Rok']).agg({'Liczba':['sum']}) # - sumę wszystkich urodzonych dzieci w całym danym okresie,\
print(dzieci)
dzieci.plot()
plt.show()
