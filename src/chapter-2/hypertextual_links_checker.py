
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

def execute():
    print("ESERCIZIO 1 - CAPITOLO 2")
    url = input("Inserire l'url: ")
    scraper = DataScraper()

    soup = scraper.html_data_scraper(url)

    links = [(link.string, link["href"])
             for link in soup.find_all("a")
             if link.has_attr("href")
                if "http" in str(link["href"]).lower()]
    
    [print(f'{x[1]}\n') for x in links]

    [scraper.html_test_connection(str(x[1])) for x in links]
