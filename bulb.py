word = input("Enter a message: ")

# Convert each character to its ASCII number
ascii_num = [ord(c) for c in word]    #the iteration aint working like the way i want it to , will certainly come back later to debug but for now namaste

# Convert the ASCII number to binary
binary = []
for num in ascii_num:
    temp = []
    while num > 0:
        temp.append(num % 2)
        num //= 2
    binary.append(temp[::-1])

j = len(binary[-1]) - 1
if j >= 0 and binary[-1][j] == 0:
    # Dark emoji
    print("\U000026AB")
else:
    # Light emoji
    print("\U0001F7E1")
