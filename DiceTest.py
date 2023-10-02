import math
import random

def rollDie(minInt, maxInt, weight, weightPower, weightSpread)
    try: # Make sure all arguments are valid
        int(minInt)
        int(maxInt)
        if weight:
            float(weight)
            float(weightPower)
            float(weightSpread)
    except:
        return None
    if not wieght:
        return random.randrange(minInt, maxInt)
    elif weight >= minInt and weight <= maxInt and weightPower >= 1:
        result = weight
        distort = math.log(random.uniform(2**
    else:
        return None

dTwenty = 0
dTwenty = math.ceil(random.random() * 20)
print(dTwenty)
