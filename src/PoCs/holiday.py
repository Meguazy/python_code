import holidays
import numpy as np
import pendulum

def main():
    it_festivities = holidays.IT(years=range(2023,2029))
    string_holidays = "FORMATO DELLE DATE: gg-mm-YY\n\n"
    current_year = "none"

    for key, value in it_festivities.items():
        if current_year == "none" or current_year != key.year:
            string_holidays += "\n\n-----ANNO " + str(key.year) + "-----\n\n"
            current_year = key.year

        key_formatted = key.strftime('%d-%m-%Y')
        string_holidays += key_formatted + " -> " + value + "\n"

    with open("date.txt", "w") as file:
        file.write(string_holidays)

if __name__ == "__main__":
    main()