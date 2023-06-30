import math
import numpy as np
import pandas as pd

trunc = lambda x: math.trunc(1000*x)/1000
pd.set_option('display.max_columns', 200)
lynx_dataset = pd.read_csv("lynx.csv",
                           header=0)

#Reconstructing the NaN data with the mean value of the column
lynx_count_column = lynx_dataset["Lynx_boreal"]
clean_data = lynx_count_column.notnull()
lynx_count_column[-clean_data] = lynx_count_column[clean_data].mean()

#1ST METHOD - ARITHMETICAL
group = (lynx_dataset["Year"]//10)*10
grouped = lynx_dataset.groupby([group]).sum()
grouped.index.names = ["Decade"]

print(grouped.sort_values("Lynx_boreal", ascending=False).applymap(trunc).head(50)["Lynx_boreal"])

#2ND METHOD - USING THE 'CUT' FUNCTION
years = list(range(1940,2021,10))
group_2 = pd.cut(lynx_dataset["Year"], 
                 bins=years, 
                 labels=years[:-1])
grouped_2 = lynx_dataset.groupby(group_2).sum()
grouped_2.index.names = ["Decade"]
by_decade = grouped_2.sort_values("Lynx_boreal", ascending=False).applymap(trunc)["Lynx_boreal"]

by_decade.to_csv("by_decade.csv")