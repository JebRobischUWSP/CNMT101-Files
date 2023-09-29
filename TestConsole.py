import os
import time
import keyboard # Remember to pip those requirements

exitDialog = 0
dims = [20,16]
currentPos = [0,0]
lightLevel = [".","░","▒","▓"]

def changePos(x,y):
    currentPos[0] += x
    currentPos[1] += y
    if currentPos[0] < 0:
        currentPos[0] = 0
    elif currentPos[0] > dims[0]:
        currentPos[0] = dims[0]
    if currentPos[1] < 0:
        currentPos[1] = 0
    elif currentPos[1] > dims[1]:
        currentPos[1] = dims[1]
def enableExitDialog(): # >:(
    global exitDialog
    exitDialog = 1

keyboard.add_hotkey('left', changePos, args=[-1,0], suppress=True, timeout=0.1)
keyboard.add_hotkey('right', changePos, args=[1,0], suppress=True, timeout=0.1)
keyboard.add_hotkey('up', changePos, args=[0,-1], suppress=True, timeout=0.1)
keyboard.add_hotkey('down', changePos, args=[0,1], suppress=True, timeout=0.1)
keyboard.add_hotkey('escape', enableExitDialog, suppress=True, timeout=.5)
_ = os.system('cls')
oldPos = None

while(True):
    if exitDialog >= 1:
        _ = os.system('cls')
        print("Would you like to exit? (Y/N)")
        x = input()
        while not (x == "y" or x == "Y" or x == "n" or x == "N"):
            x = input("Please input Y or N")
        if x == "y" or x == "Y":
            break;
        else:
            exitDialog = 0;
    elif oldPos != currentPos:
        _ = os.system('cls')
        space = [None] * dims[1]
        for i in range(dims[1]):
            space[i] = ["█"] * dims[0]
        # Modify Space Array
        space[currentPos[1]][currentPos[0]] = "@"
        for i in range(dims[0]):
            for j in range(dims[1]):
                dist = max(abs(i - currentPos[1]), abs(j - currentPos[0]))
                if dist > 0 and dist <= len(lightLevel):
                    try:
                        space[i][j] = lightLevel[dist - 1]
                    except:
                        _ = None # Do nothing to supress error
        for i in range(dims[1]):
            print("".join(space[i]))
        print(str(currentPos[0]) + ", " + str(currentPos[1]) + " -- " + str(exitDialog))
        oldPos = [currentPos[0], currentPos[1]]
    time.sleep(.1)