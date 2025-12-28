x_str, y, z_str = input("Expression: ").split(" ")

x = float(x_str)
z = float(z_str)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("Invalid")
