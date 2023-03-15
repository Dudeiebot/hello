
while True:  #used instead of a do while loop that python does not have but we need user input to be true  
    height = int(input("Tell me the Height: "))
    if height >= 0 and height <= 15:
        break
    else:
        print("please a number between 0 and 15")

for i in range(height):
    print(' ' * (height - i - 1) + '#' * (i + 1) + '  ' + '#' * (i + 1)) #added some other shiit for mario more