from bs4 import BeautifulSoup
from collections import Counter
from nltk import word_tokenize
from nltk import PorterStemmer
from nltk import download
from nltk.corpus import stopwords
from urllib.request import urlopen

download('punkt')
download('stopwords')

def basic_tokenizer():
    ls = PorterStemmer()

    with urlopen(input("Inserire URL: ")) as doc:
        soup = BeautifulSoup(doc, features="html.parser")

    #Extract and reduce the text into tokens
    words = word_tokenize(soup.text)

    #Make everything lowercase
    words = [w.lower() for w in words]

    #Let's get rid of useless words by using the radicals
    words = [ls.stem(w)
             for w in words
                if w not in stopwords.words("english") and w.isalnum()
            ]
    
    #Inizializza il contatore con le frequenze
    freqs = Counter(words)

    #Stampa le 10 più comuni
    print(f"Le 10 parole più frequenti sono:\n {freqs.most_common(10)}")