def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def check_length(s):
    return 2 <= len(s) <= 6

def number_placement(s):
    seen_digit = False
    for i in s:
        if i.isdigit():
            if not seen_digit:
                if i == "0":
                    return False
                seen_digit = True
        else:
            if seen_digit:
                return False
    return True


def valid_characters(s):
    for i in s:
        if not i.isalnum():
            return False
    return True

def two_letter_start(s):
    return s[0].isalpha() and s[1].isalpha()

def is_valid(s):
    return (
        check_length(s)
        and number_placement(s)
        and valid_characters(s)
        and two_letter_start(s)
    )

main()
