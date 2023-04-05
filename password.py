from string import digits
from itertools import product

for passcode in product(digits, repeat=4):
    print (*passcode)


from string import ascii_letters, digits, punctuation
from itertools import product

for passcode in product(ascii_letters + digits + punctuation, repeat=4):
    print (*passcode)




""""
So here technically we are making sure to check the possibility of a 4 digit password in the first code and i mean checking 0123456789 and coming out with all possible amount
of 4 password that can be formed from it and the second one is adding letters with numbers and also punctuation together to check for the possible amount of password theat can be formed from using it.
Hereby i want you to under stand that it all depends on the amount of the occurence will happen like, for example in a 4 digit password that only takes in digits without letter 
and puntuation the occurrence is 10000 and it can be very easy to crack for real

"""