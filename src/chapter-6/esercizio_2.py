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

#Creating GDP per capita dataframe
GDP_per_capita = pd.concat(pd.read_html(str(GDP_per_capita_html), index_col=0))
#Cleaning the data inside the index
new_index = list(map(lambda s: s.replace("\u202f*",""), GDP_per_capita.index.values))
GDP_per_capita.index = new_index
print(GDP_per_capita)