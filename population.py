

start = 0
while start < 9:
    start = int(input("Enter the current population: ")) #returning the input from the user as an int just like converting it

end = 0
while end < start:
    end = int(input("Enter the forecasted population: "))

years = 0
while start < end:
    start = (start + start / 3 - start / 4)
    years += 1

print(f"It will take {years} years to reach a population of {end}.")