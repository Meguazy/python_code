import numpy as np
import pandas as pd

print("------ 1:LE SERIE ------")

inflation = pd.Series((2.2, 3.4, 2.8, 1.6, 2.3, 2.7, 3.4, 3.2, 2.8, 3.8, 0.4, 1.6, 3.2, 2.1, 1.5, 1.5))

#Lunghezza della serie
print(f"\nLunghezza della serie: {len(inflation)}")

#Valori dell'array
print(inflation.values)

#Step dell'indice
print(inflation.index)

#Valori dell'indice
print(inflation.index.values)

#Modifico l'ultimo elemento
inflation.values[-1] = 1.6
print(inflation.values)

#Modifico la serie con degli indici personalizzati
inflation.index = pd.Index(range(1999,2015))
inflation[2015] = np.nan
print("\nInflation con indici custom:\n")
print(inflation)

#Modifico i nomi degli indici e dei valori dell'array
inflation.index.name = "Year"
inflation.name = "%"
print("\nInflation con i nomi modificati:\n")
print(inflation)

#Estraggo i 5 elementi di testa e di coda della serie
print("\n5 elementi di coda:")
print(inflation.tail())
print("5 elementi di testa:")
print(inflation.head())

print("------ 2:I FRAME ------")
#Creo un dataframe
alco2009 = pd.DataFrame([(1.20, 0.22, 0.58),
                         (1.31, 0.54, 1.16),
                         (1.19, 0.38, 0.74)],
                         columns=("Beer", "Wine", "Spirits"),
                         index=("Alabama", "Alaska", "Altri stati"))

print(alco2009)

#alternativa alla creazione
alco2009 = pd.DataFrame({"Beer" : (1.20, 0.22, 0.58),
                         "Wine" : (1.31, 0.54, 1.16),
                         "Spirits" : (1.19, 0.38, 0.74)},
                         index=("Alabama", "Alaska", "Altri stati"))

