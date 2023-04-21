import first_tokenizer_example as fte

from hypertextual_links_checker import DataScraper

def execute_ex_1():
    print("ESERCIZIO 1 - CAPITOLO 2")
    url = input("Inserire l'url: ")
    scraper = DataScraper()

    soup = scraper.html_data_scraper(url)

    links = [(link.string, link["href"])
             for link in soup.find_all("a")
             if link.has_attr("href")
                if "http" in str(link["href"]).lower()]
    
    [scraper.html_test_connection(str(x[1])) for x in links]

def main():
    print("Chapter 2 \n")
    menu = int(input("Inserisci il programma che vuoi avviare: "))
    if menu == 0:
        fte.basic_tokenizer()
    elif menu == 1:
        execute_ex_1()

if __name__ == "__main__":
    main()