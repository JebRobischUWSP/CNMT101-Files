import math
import random

def rollDie(minInt, maxInt, weightValue, weightBase, weightPower):
    try: # Make sure all arguments are valid
        int(minInt)
        int(maxInt)
        if weightValue:
            float(weightValue)
            float(weightBase)
            float(weightPower)
    except:
        return None
    if not weightValue:
        return random.randrange(minInt, maxInt)
    elif weightValue >= minInt and weightValue <= maxInt and weightBase > 1 and weightBase <= 10 and weightPower > 0 and weightPower <= 50:
        distort = math.log(random.uniform(1, weightBase**weightPower), weightBase) / weightPower
        if random.randint(0,1) == 1:
            return maxInt - round((maxInt - weightValue) * distort)
        else:
            return minInt + round((weightValue - minInt) * distort)
    else:
        return None

rollTotal = 0
for i in range(10000):
    diceRoll = rollDie(1, 20, 4, 3, 2)
    rollTotal += diceRoll
    if i % 100 == 0:
        print(diceRoll)

print(rollTotal)
print(rollTotal / 10000)
