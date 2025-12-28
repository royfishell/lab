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
    print(f"{year}-{month:02}-{day:02}")


def get_date():
    while True:
        date = input("Date: ").strip()

    # Case 1: numeric format (3/25/1993)
        if "/" in date:
            parts = date.split("/")
            if len(parts) != 3:
                continue
            month_str, day_str, year_str = parts

    # Case 2: text format (March 25, 1993)
        else:
            parts = date.split()
            if len(parts) !=3:
                continue
            month_name, day_raw, year_str = parts

            if month_name not in months:
                continue

            month_number = months.index(month_name) + 1
            month_str = str(month_number)

            day_str = day_raw[0:-1]
            
        try:
            month = int(month_str)
            day = int(day_str)
            year = int(year_str)
        except ValueError:
            continue

        if 1 <= month <= 12 and 1 <= day <= 31:
            return month, day, year


main()
