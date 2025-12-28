deep = input("What is the question to the Great Question of Life, the Universe, and Everything? ")

match deep.lower().strip():
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
