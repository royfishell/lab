from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(fonts))

elif len(sys.argv) == 3:
    flag = sys.argv[1]
    font_name = sys.argv[2]

    if flag not in ["-f", "--font"]:
        sys.exit("Invalid usage")

    if font_name not in fonts:
        sys.exit("Invalid usage")

    figlet.setFont(font=font_name)

else:
    sys.exit("Invalid usage")

s = input("Input: ")
print(figlet.renderText(s))
