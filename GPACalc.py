import os
import time

classList = []

while(True):
    _ = os.system('cls')
    print("GPA Calculator 0.1 - Now with Removing!        Tip: Type 'cancel' to cancel any operation!\nType 'g' to Input a Grade, 'r' to Remove a Grade, 'c' to Calculate Cumulative GPA, or Type 'e'/'exit' to Exit")
    if len(classList) > 0:
        for i in range(len(classList)):
            print(" > Class " + str(i) + ": GPA - " + str(classList[i][0]) + " || Credits - " + str(classList[i][1]))
    else:
        print(" > No Classes Added Yet!")
    userIn = input("\nType an Option: ")
    if userIn == "g" or userIn == "G":
        classList.append([-1,-1]) # Add entry to classList
        while(True):
            grade = input("Type your class's GPA: ")
            if grade == 'cancel': break
            try:
                grade = float(grade)
            except:
                print("Bad value!")
                continue
            if grade > 4 or grade < 0:
                print("Out of GPA range! (0-4)")
                continue
            else:
                classList[len(classList)-1][0] = grade
                break
        if classList[len(classList)-1][0] == -1:
            classList.pop()
            continue
        while(True):
            creditHours = input("Type your class's credit-hours: ")
            if creditHours == 'cancel': break
            try:
                creditHours = float(creditHours)
            except:
                print("Bad value!")
                continue
            if creditHours <= 0:
                print("Your class must be worth more than 0 credits!")
                continue
            else:
                classList[len(classList)-1][1] = creditHours
                break
        if classList[len(classList)-1][1] == -1:
            classList.pop()
            continue
    elif userIn == "c" or userIn == "C":
        if len(classList) <= 0:
            print("No Grades inputted yet.")
        else:
            sumGrades = 0
            sumCredits = 0
            sumWeighted = 0
            for i in range(len(classList)): # Sum can't be used due to nested lists
                sumGrades += classList[i][0]
                sumCredits += classList[i][1]
                sumWeighted += classList[i][0]*classList[i][1]
            print("Average GPA Per-Class: " + "{:.2f}".format(sumGrades / len(classList)))
            print("Overall Credits:       " + "{:.2f}".format(sumCredits))
            print("Cumulative GPA:        " + "{:.2f}".format(sumWeighted / sumCredits))
        input("Press enter to continue")
    elif userIn == "r" or userIn == "R":
        while(True):
            toRemove = input("Type the # of the class to remove: ")
            if creditHours == 'cancel': break
            try:
                toRemove = int(toRemove)
            except:
                print("Bad value!")
                continue
            if toRemove < 0 or toRemove >= len(classList):
                print("You must choose an existing class entry!")
                continue
            else:
                classList.pop(toRemove)
                break
    elif userIn == "exit" or userIn == "Exit" or userIn == "e" or userIn == "E":
        break
    else:
        input("Invalid Input. Press enter to reset")