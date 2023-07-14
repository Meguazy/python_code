import numpy as np
import pandas as pd

from miner import Miner

#alco_per_capita.to_csv("ex_2_csvs/alco_per_capita.csv", index="Country")
#GDP_per_capita.to_csv("ex_2_csvs/GDP_per_capita.csv")
alco_per_capita_html = Miner.table_miner("https://en.wikipedia.org/wiki/List_of_countries_by_alcohol_consumption_per_capita", 2)
GDP_per_capita_html = Miner.table_miner("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita", 1)

#Creating alco per capita dataframe
alco_per_capita = pd.concat(pd.read_html(str(alco_per_capita_html), index_col='Country'))
print(alco_per_capita)

#Creating GDP per capita dataframeEcco
GDP_per_capita = pd.concat(pd.read_html(str(GDP_per_capita_html), index_col=0))
#Cleaning the data inside the index
new_index = list(map(lambda s: s.replace("\u202f*",""), GDP_per_capita.index.values))
GDP_per_capita.index = new_index
print(GDP_per_capita)

alco_over_mean_value = alco_per_capita["Total"] > alco_per_capita["Total"].mean()
print(alco_over_mean_value)
GDP_over_mean_value = GDP_per_capita['CIA[8][9][10]']['Estimate'] > GDP_per_capita['CIA[8][9][10]']['Estimate'].mean()

cross_table_over = pd.crosstab(GDP_over_mean_value, alco_over_mean_value).unstack()

data = pd.DataFrame({"under_alco_num": cross_table_over.groupby("Total").sum().iloc[0],
                     "over_alco_num": cross_table_over.groupby("Total").sum().iloc[1],
                     "over_alco_over_GDP": cross_table_over.iloc[3],
                     "over_alco_under_GDP": cross_table_over.iloc[2],
                     "under_alco_over_GDP": cross_table_over.iloc[1],
                     "under_alco_under_GDP": cross_table_over.iloc[0]},
                     index=["Val"])
print(data)
print("\n----ANALISI STATI CON UN CONSUMO DI ALCOOL SUPERIORE ALLA MEDIA----")
print("Percentuale di stati sopra alla media per consumo di alcool che hanno GDP sopra alla media:")
print(str(data["over_alco_over_GDP"].values[0] / data["over_alco_num"].values[0] * 100) + "%")
print("Percentuale di stati sopra alla media per consumo di alcool che hanno GDP sotto alla media:")
print(str(data["over_alco_under_GDP"].values[0] / data["over_alco_num"].values[0] * 100) + "%")

print("\n----ANALISI STATI CON UN CONSUMO DI ALCOOL INFERIORE ALLA MEDIA----")
print("Percentuale di stati sotto alla media per consumo di alcool che hanno GDP sopra alla media:")
print(str(data["under_alco_over_GDP"].values[0] / data["under_alco_num"].values[0] * 100) + "%")
print("Percentuale di stati sotto alla media per consumo di alcool che hanno GDP sotto alla media:")
print(str(data["under_alco_under_GDP"].values[0] / data["under_alco_num"].values[0] * 100) + "%")