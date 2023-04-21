
from urllib.request import urlopen

from bs4 import BeautifulSoup

class DataScraper():

    def html_data_scraper(self, url: str) -> BeautifulSoup:
        try:
            with urlopen(url) as doc:
                soup = BeautifulSoup(doc, features="html.parser")
                print(f"Il collegamento '{url}' funziona")
        except:
            print(f"Il collegamento '{url}' non funziona")
        return soup
    
    def html_test_connection(self, url: str) -> None:
        try:
            with urlopen(url, timeout=3) as doc:
                BeautifulSoup(doc, features="html.parser")
                print(f"Il collegamento '{url}' funziona")
        except:
            print(f"Il collegamento '{url}' non funziona")

