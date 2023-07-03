from bs4 import BeautifulSoup
from nltk import word_tokenize
from urllib.request import urlopen

import pandas as pd

class Miner():
    def table_miner(url: str, table_position: str):
        try:
            with urlopen(url) as doc:
                soup = BeautifulSoup(doc, features="html.parser")
                table = soup.find_all("table")[table_position]            
        except:
            print("There was an error while fetching the table")
        return table