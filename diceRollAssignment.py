#import os
#import math
import random

"""
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
print('Welcome to diceRoll! Would you like to roll some dice? (Y/N)')
userIn = input('> ')
if userIn = 'y':
    print('How many sides do you want per die?')
    sides = input('> ')
    print('...and how many dice do you want to roll?')
    dice = input('> ')
    if int(sides) and sides >= 2 and int(dice) and dice >= 1:
        



    
