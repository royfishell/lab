while True:
    x, y = input("Fraction: ").split("/")
    try:
        percentage = (int(x)/int(y))*100
        if not 0 <= percentage <= 100:
            raise ValueError()
        else:
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{int(percentage)}%")
