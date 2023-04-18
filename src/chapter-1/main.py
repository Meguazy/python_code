import collections
import os
import pickle
import re

from web_scraper import WebScraper
from collections import Counter

def countWordsFromPattern(pattern: str, html: str):
    pattern_words = re.findall(pattern, html, re.I)
    cntr = Counter(pattern_words)
    common = dict(cntr.most_common())
    print(common)

def getWordsListFromPattern(pattern: str, to_be_searched: str):
    return re.findall(pattern, to_be_searched, re.I)

def mergeDicts(dicts: list) -> dict:
    super_dict = collections.defaultdict(list)
    for d in dicts:
        for k, v in d.items():
            super_dict[k].append(v)

    return super_dict

def main():
    #Scraping words from a website and counting them
    string_html = WebScraper.webScraperFromString(str(input("Inserisci l'url che vuoi ricercare: ")))
    countWordsFromPattern(r"\w{3,50}", string_html)
    countWordsFromPattern(r"\w+", string_html)

    #Indexing files in a folder using dicts
    path = input("Inserisci il path in cui vuoi cercare i file: ")
    file_list = os.listdir(path)
    dicts: list = []

    for file_name in file_list:
        with open(f"{path}{file_name}", mode="r") as f:
            text = str(f.read())
            words_list = getWordsListFromPattern(r"\w+", text)
            dicts.append(dict.fromkeys(words_list,file_name))
            
    words_dict = mergeDicts(dicts)

    with open("pickle_files/myData.pickle", "wb") as oFile:
        pickle.dump(words_dict, oFile)

    with open("pickle_files/myData.pickle", "rb") as iFile:
        data = pickle.load(iFile)
        print(data)

if __name__ == "__main__":
    main()