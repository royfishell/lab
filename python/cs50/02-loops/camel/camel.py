def main():
    camel = input("camelCase: ")
    print(make_snake(camel))

def make_snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            snake += "_" + char.lower()   
        else:
            snake += char

    return snake
            

main()
