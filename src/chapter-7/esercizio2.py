import community as cm
import networkx as nx
import pandas as pd

from miner import Miner

shakespear_table = Miner.table_miner("https://shakespeare.mit.edu", 1)

shakespear_df = pd.concat(pd.read_html(str(shakespear_table)))

shakespear_df.to_csv("opere.csv")