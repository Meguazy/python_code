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
tall_alco = alco_re.stack()
print(tall_alco)

tall_alco.index.names = ['State', 'Year', 'Drink']
print(tall_alco.head(10))

print("\nUnstacking:")
wide_alco = alco_re.unstack()
print(wide_alco.head(10))
print("\n\n\n\n")
print(wide_alco.Beer)

print("\nPivoting:")
print(alco_re.pivot_table(index='Year', columns='State', values=['Wine']))

print("\n---UNIT 33:HOW TO MANAGE MISSING DATA---")
print("\nDeleting missing data:")
print(alco_nan.dropna(how="all"))
print(alco_nan.dropna(how="all",axis=1))
print(alco_nan.dropna())

print("\nRecostructing missing data")
sp = alco_nan["Wine"]
clean = sp.notnull()
#In this case i'm replacing the non clean value with the mean of the clean ones
sp[-clean] = sp[clean].mean()
print(alco_nan.head())

#In this other case i'm replacing thhe non clean values with zeros
print(alco_nan.fillna(0))

#In this last case i'm replacing the non clean values using the method='ffill' parameter
print(alco_nan.fillna(method="ffill"))

print("\nReplacing missing data")
print(alco_nan.replace(np.nan,"Hello"))


#Merging data - Unit 34
alco2009.drop("Total", axis=1, inplace=True)
print("\nMerge function:")
population = pd.DataFrame({"Population" : [631543, 599657, 544270, 698712]},
                          index=("Alabama", "Alaska", "Altri stati", "Ohio"))
population.index.name = "Stati"
print(population.head())
print("\nMerged population and alco")
merged = pd.merge(alco2009.reset_index(),population.reset_index()).set_index("Stati")
print(merged.head())

#CONCAT 
print("\nConcatenating population and alco2009")
print(pd.concat([alco2009, population], axis=1).head())

#SORTING
print("\nSorting the frame by index:")
pop_by_state = population.sort_index(ascending=False)
print(pop_by_state.head())

print("\nSorting the frame by values:")
print(population.sort_values("Population",ascending=False).head())

#INDEX CLASSIFICATION
print("\nUsing the 'rank' function to rank the frame")
print(pop_by_state.rank().head())

#STATISTICA DESCRITTIVA
print("\n Max function on the columns:")
print(alco2009.max())
print("\n Min function on the rows:")
print(alco2009.min(axis=1))
print("\n Sum function on the columns:")
print(alco2009.sum())
print("\n Cumulative sum function on the columns for the Alabama state:")
print(alco_re.loc["Alabama"])
print(alco_re.loc["Alabama"].cumsum().head())
print("\n Progressive difference function on the columns for the Alabama state:")
print(alco_re.loc["Alabama"].diff().head())

#UNICITA', CONTEGGIO E APPARTENENZA
dna = "AGTCCGCGAATACAGGCTCGGT"
dna_as_series = pd.Series(list(dna), name="genes")
print(dna_as_series.head())

print("\n unique function on dna Series:")
print(dna_as_series.unique())
print("\n values_counts function on dna Series:")
print(dna_as_series.value_counts().sort_index())

print("\n isin function on dna seriesm, using the 'all' parameter:")
valid_nucs = list("ACGT")
print(dna_as_series.isin(valid_nucs).all())

#---TRASFORMAZIONE DEI DATI - UNIT 36---
print("\n Using the sum function on the 'Total' column:")
alco2009["Total"] = alco2009[list(alco2009.columns)].sum(axis=1)
print(alco2009.head())

print("\n Using log10 numpy function on the 'Total' column:")
print(np.log10(alco2009.Total).head())

#Aggregations
print("\nAggregation by Year using sum function:")
alco_noidx = alco_re.reset_index()
sum_alco = alco_noidx.groupby("Year").sum().drop("State", axis=1)
print(sum_alco.head())
print("\n Aggregation using for loop:")
for year, year_frame in alco_noidx.groupby("Year"):
    print(year)
    print(year_frame)

#Discretizzazione
print("\nDiscretizzzione senza labels")
cats = pd.cut(alco2009["Wine"], 3)
print(cats.head())

print("\nDiscretizzzione con labels")
cats = pd.cut(alco2009["Wine"], 3, labels=("Low", "Moderate", "Heavy"))
print(cats.head)

print("\n Discretizzazione con i quantili:")
quants = pd.qcut(alco2009["Wine"], 3, labels=("Low", "Moderate", "Heavy"))
print(quants.head())

#Mappaggio
print("\n Using map function to get the suffix of the state and turn it to upper case:")
with_state = alco2009.reset_index()
suffix = with_state["Stati"].map(lambda x: x[:3].upper())
print(suffix.head()) 

#Tabulazione incrociata
print("\n Using crosstab to check if a wine state (a state where the wine consumption is higher than the mean) is also a beer state:")
wine_state = alco2009["Wine"] > alco2009["Wine"].mean()
beer_state = alco2009["Beer"] > alco2009["Beer"].mean()
print(pd.crosstab(wine_state,beer_state))

#--- I/O SU FILE IN PANDAS ---
print("\n Reading a CSV file through Pandas:")
regions = pd.read_csv("data.csv",
                      header=None,
                      names=("region", "division", "state"))
regions = regions.fillna("prova")
print(regions.head(regions.shape[0]))

print("\n Cleaning the DataFrame:")
state2reg_series = regions.ffill().set_index("state")["region"]
print(state2reg_series.head())
#Converting state2reg_series to a dict object
state2reg = state2reg_series.to_dict()
#Writing on a csv
regions.to_csv("prova.csv")
#Chunking
print("\n Using chunking:")
chunker = pd.read_csv("prova.csv", 
                      chunksize=5, 
                      header=None,
                      names=("region", "division", "state"))
accum = pd.Series()
for piece in chunker:
    counts = piece["region"].value_counts()
    accum = accum.add(counts, fill_value=0)
    print("\n Accum:")
    print(accum)

