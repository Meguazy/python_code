import first_tokenizer_example as fte
import hypertextual_links_checker as hlc

def main():
    print("Chapter 2 \n")
    menu = int(input("Inserisci il programma che vuoi avviare: "))
    if menu == 0:
        fte.basic_tokenizer()
    elif menu == 1:
        hlc.execute()

if __name__ == "__main__":
    main()