def main():
    time = input("What time is it? ")
    converted_time = convert(time)
    
    if 7 <= converted_time <= 8:
        print("Breakfast time")
    elif 12 <= converted_time <= 13:
        print("Lunch time")
    elif 18 <= converted_time <= 19:
        print("Dinner time")
    
def convert(time):
    hours, minutes = time.split(":")
    converted_time = float(hours) + (float(minutes) / 60)
    return converted_time

if __name__ == "__main__":
    main()
