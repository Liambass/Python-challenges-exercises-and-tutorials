# Create 2 new Python files. In one file, write a function that will generate a number between 1 and 6. Make this a module called dice.
# In the second file, use the dice module to simulate throwing 2 dice and print the values you get from the dice.

import diceroll

dx = int(input("d? "))
nx = int(input("number of rolls? "))

total = 0
i = 0

if (dx == 10 and nx == 2):
    total = diceroll.percentile()
else:
    while i < nx:
        total += diceroll.diceroll(dx)
        i += 1


print(total)