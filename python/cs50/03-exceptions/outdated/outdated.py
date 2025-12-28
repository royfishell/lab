months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    month, day, year = get_date()
    print(f"{year}-{int(month):02}-{int(day):02}")


def get_date():
    while True:
        date = input("Date: ")
        try:
            month_name, day_raw, year = date.split()
            month = months.index(month_name) + 1
            day = day_raw[0:-1]
        except ValueError:
            try:
                month, day, year = date.split("/")
            except ValueError:
                pass
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            return month, day, year

main()
