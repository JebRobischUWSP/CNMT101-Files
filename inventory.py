#Inventory Variable block
inv1 = 'key'
inv2 = '+1Hit' #TODO Name it!!!
inv3 = 'coins'
inv4 = 'potion'

invArr = [inv1,inv2,inv3,inv4];

def printInv(num = None):
    if num is None:
        print("Your inventory contains:\n")
        for i in range(len(invArr)): #I'm way too used to numerical for loops :/
            print('> ' + invArr[i]);
    else:
        print("Item " + str(num) + " is: " + invArr[num]);

invArr.append('Bonus ducks!')
invArr.append('Fear of Gryla')

printInv()
printInv(1)
