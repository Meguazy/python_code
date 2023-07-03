import ssl
from bs4 import BeautifulSoup
from nltk import word_tokenize
from urllib.request import urlopen

import pandas as pd

class Miner():
    def table_miner(url: str, table_position: int):
        print("\nProva:")
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        ctx.set_ciphers('DEFAULT:!DH')
        with urlopen(url, context=ctx) as doc:
                
                soup = BeautifulSoup(doc, features="html.parser")
                table = soup.find_all("table")[table_position]            
                print(table)
        try:
            print("\nProva:")          
        except:
            print("There was an error while fetching the table")
        return table