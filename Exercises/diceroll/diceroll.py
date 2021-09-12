# Create 2 new Python files. In one file, write a function that will generate a number between 1 and 6. Make this a module called dice.
# In the second file, use the dice module to simulate throwing 2 dice and print the values you get from the dice.

import random

def diceroll(x):
    if x == 10:
        return random.randint(0, 9)
    else:
        return random.randint(1, x)

def percentile():
    return random.randint(1,100)
