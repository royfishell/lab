import inflect
p = inflect.engine()

names = []

try:
    while True:
        name = input("Names: ").strip()
        if name:
            names.append(name)

except EOFError:
    print()
    phrase = p.join(names)
    print(f"Adieu, adieu, to {phrase}.")
