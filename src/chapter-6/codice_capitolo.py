import numpy as np
import pandas as pd

def trunc_c(values, decs=0):
    return np.trunc(values*10**decs)/(10**decs)

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
alco2009_2 = pd.DataFrame([(1.20, 0.22, 0.58),
                         (1.31, 0.54, 1.16),
                         (1.19, 0.38, 0.74)],
                         columns=("Beer", "Wine", "Spirits"),
                         index=("Alabama", "Alaska", "Altri stati"))
alco2009_2.index.name = "Stati"

#alternativa alla creazione
alco2009 = pd.DataFrame({"Beer" : (1.20, 0.22, 0.58, 1.3),
                         "Wine" : (1.31, 0.54, 1.16, 1.3),
                         "Spirits" : (1.19, 0.38, 0.74, 1.3)},
                         index=("Alabama", "Alaska", "Altri stati", "Ohio"))

alco2009.index.name = "Stati"

print(alco2009)

#Stampo la testa della colonna Wine
print("\nTesta colonna Wire:")
print(alco2009["Wine"].head())

#Stampo la coda della colonna Beer
print("\nCoda colonna Beer:")
print(alco2009.Beer.tail())

#Setto la colonna "Total" a 0. Dato che non esiste, verrà creata
alco2009["Total"] = 0
print("\nTesta con Total = 0:")
print(alco2009.head())

#INDICIZZAZIONE
print("\n---INDICIZAZZIONE---")
#Setto un nuovo indice
alc_reset = alco2009.reset_index().set_index("Beer")
print("\nIndice resettato:")
print(alc_reset.head())

#Utilizzo dell'attributo 'loc'
print("\nProva loc")
print(alco2009.loc["Alaska"])

#Ricerca dell'indice
print("\nRicerca dell'indice 'Samoa':")
print("Samoa" in alco2009.index)

#REINDICIZZAZIONE
s_state = [state for state in alco2009.index if state[0] == 'A'] + ["Samoa"]
drinks = list(alco2009.columns) + ["Water"]
alco_nan = alco2009.reindex(s_state,columns=drinks)
print("\nReindexed frame:")
print(alco_nan.head())

#INDICIZAZZIONE GERARCHICA
print("\n---INDICIZAZZIONE GERARCHICA---")
multi = pd.MultiIndex.from_tuples((("Alabama", 1977),("Alabama", 1978),("Alabama", 1979),
                                  ("Alaska", 1977),("Alaska", 1978),("Alaska", 1979),
                                  ("Altri stati", 1977),("Altri stati", 1978),("Altri stati", 1979),
                                  ("Ohio", 1977),("Ohio", 1978),("Ohio", 1979)),
                                  names=["State", "Year"]
                                )

print("\nMulti indice:")
alco_re = alco2009.reindex(multi)

alco_re.Beer = np.ones(12) * trunc_c(np.random.uniform(0,3,size=12),2)
alco_re.Wine = np.ones(12) * trunc_c(np.random.uniform(0,3,size=12),2)
alco_re.Spirits = np.ones(12) * trunc_c(np.random.uniform(0,3,size=12),2)
alco_re.Total = alco_re[list(alco_re.columns)].sum(axis=1)

print(alco_re)

print("\nUtilizzo di 'loc' per Alaska")
print(alco_re.loc["Alaska"])
print("\nUtilizzo di 'loc' per Alaska e anno 1979")
print(alco_re.loc["Alaska", 1979])

#STACK E PIVOT
print("\n---STACK E PIVOT---")