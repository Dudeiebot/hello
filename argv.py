import sys
from pyfiglet import Figlet

if len(sys.argv) != 3:
    sys.exit(1)
text = input("INPUT: ")

figlet = Figlet()
figlet.getFonts()
figlet.setFont(font = sys.argv[2])
print(figlet.renderText(text))