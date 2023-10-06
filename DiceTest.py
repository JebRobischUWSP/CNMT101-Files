import math
import random

def rollDie(minInt, maxInt, weightValue = None, weightBase = None, weightPower = None):
    try: # Make sure all arguments are valid
        minInt = int(minInt)
        maxInt = int(maxInt)
        if weightValue:
            weightValue = float(weightValue)
            weightBase = float(weightBase)
            weightPower = float(weightPower)
    except:
        return None
    if not weightValue:
        return random.randint(minInt, maxInt)
    elif weightValue >= minInt and weightValue <= maxInt and weightBase > 1 and weightBase <= 10 and weightPower > 0 and weightPower <= 50:
        distort = math.log(random.uniform(1, weightBase**weightPower), weightBase) / weightPower
        if random.randint(0,1) == 1:
            return maxInt - round((maxInt - weightValue) * distort)
        else:
            return minInt + round((weightValue - minInt) * distort)
    else:
        return None

def roll20Set(dieAmount):
    for rolls in range(dieAmount):
        rollResult = rollDie(1, 20)
        addedText = ''
        if rollResult == 20:
            addedText = ' >>>         Crit Success!'
        elif rollResult == 1:
            addedText = ' >>>         Crit Fail!'
        elif rollResult >= 11:
            addedText = ' - Good Roll'
        else:
            addedText = ' -  Bad Roll'
        print(str(rollResult).rjust(2) + addedText)
    print('\n== - Dice rolled! - ==\n')

roll20Set(20)
roll20Set(5)
