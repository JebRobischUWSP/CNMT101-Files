#import os
#import math
import random

print('Welcome to diceRoll! Would you like to roll some dice? (Y/N)')
userIn = input('> ')
if userIn == 'y':
    print('How many sides do you want per die?')
    sides = int(input('> ')) # Get sides per die, parse integer
    print('...and how many dice do you want to roll?')
    dice = int(input('> ')) # Get amount of dice, parse integer
    if sides >= 2 and dice >= 1: # Minimum value check
        if sides == 20: #Duplicate for loop for d20s to remove 1 operation per roll (checking side count)
            for i in range(dice):
                result = random.randint(1, sides) # Roll d20s
                print('#' + str(i + 1) + ' - ' + str(result)) # Output result
                if result == 20:
                    print('  Critical Hit!') # Check & output Crit
                elif result == 1:
                    print('  Critical Fail!') # Check & output Fail
        else:
            for i in range(dice):
                result = random.randint(1, sides) # Roll normal dice
                print('#' + str(i + 1) + ' - ' + str(result)) # Output result


# Sources include PythonDocs (random library) and realpython.com for int()

"""
Whoops, ignore me!


while (True):
    _ = os.system('cls') # Not nessecary, clears terminal
    print("Welcome to diceRoll! Would you like to roll some dice? (Y/N)")
    exitFlag = False
    while (True):
        userIn = input("> ")
        if userIn == "n" or userIn == "N":
            input("Alright, goodbye!")
            exitFlag = True
            break
        elif userIn == "y" or userIn == "Y":
            break
        else:
            print("I didn't get that. Would you say again? Y or N.")
    if exitFlag:
        break
    print("Great! How many sides do you want on the die?") # Side Request
    sides = 0
    while (sides <= 0):
        userIn = input("> ")
        try:
            userIn = int(userIn) # Integer validation: die sides
        except:
            print("Please enter a whole number.")
            continue
        if userIn >= 2:
            sides = userIn
        else:
            print("Your die needs at least two sides!")
    print("Alright! Now, how many dice do you want to roll?") # Amount Request
    dice = 0
        while (dice <= 0):
        userIn = input("> ")
        try:
            userIn = int(userIn) # Integer validation: dice amount
        except:
            print("Please enter a whole number.")
            continue
        if userIn >= 1:
            dice = userIn
        else:
            print("You need at least 1 die!")
    print("Got it! Rolling dice now:\n") # Roll dice
    places = math.floor(math.log(dice, 10)) + 1
    if sides == 20: # Enable Criticals
        for i in range(dice):
    else:
        for i in range(dice):
    
    
# Souce: Documentation Lookup on W3Schools (mainly math library & right adjust)
"""

# https://github.com/JebRobischUWSP/CNMT101-Files
