
#define the fuctions 
def calculate_quarters(cents):
    return cents // 25

def calculate_dimes(cents):
    return cents // 10

def calculate_nickels(cents):
    return cents // 5

def calculate_pennies(cents):
    return cents

#collecting user input(cents)
cents = 0
while cents <= 0:
    cents = int(input("how much are you owing: "))

#the calculation that solves it
quarters = calculate_quarters(cents)
cents = cents - quarters * 25

dimes = calculate_dimes(cents)
cents = cents - dimes * 10

nickels = calculate_nickels(cents)
cents = cents - nickels * 5

pennies = calculate_pennies(cents)
cents = cents - pennies * 1

coins = quarters + dimes + nickels + pennies

print("Total number of coins to give:", coins)
