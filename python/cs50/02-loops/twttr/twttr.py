vowels = "aeiouAEIOU"
output = ""

for char in input("Input: "):
    if char not in vowels:
        output += char

print("Output:", output)
