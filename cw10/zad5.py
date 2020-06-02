import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv', sep=';')
ilosc = df.groupby(['Sprzedawca']).size()
wykres = ilosc.plot.bar(label='Ilość')
wykres.set_ylabel('Ilość złożonych zamówień')
wykres.set_xlabel('Sprzedawca')
wykres.legend()
plt.title('ilość złożonych zamówień przez poszczególnych sprzedawców')
plt.show()