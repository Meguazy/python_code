import holidays
import pendulum

def main():
    it_festivities = holidays.IT()
    current_date = pendulum.today().strftime('%Y-%m-%d')
    print("Current date: " + current_date)

    print(current_date in it_festivities)

    for fest in it_festivities:
        print("fest: " + str(fest))

if __name__ == "__main__":
    main()