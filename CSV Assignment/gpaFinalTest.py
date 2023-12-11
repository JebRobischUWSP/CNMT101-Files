import os
import sys
import re #Specifically to check class name syntax
#Relative path of file containing class/grade records. Must be in CSV format.
path = 'grades.csv'

checkFile = os.path.isfile(path)

if checkFile == True:

    infile = open(path, 'r')
    #class list
    classList = infile.readlines()

    #close the file
    infile.close()

else:

    print('file does not exist')
    sys.exit()

#count the number of grades
gradeLength = len(classList)-1
print(str(gradeLength) + " Classes Recognized\n")

#create a grade table
gpaList = {'A': 4., 'A-': 3.67, 
    'B+': 3.33, 'B': 3., 'B-': 2.67,
    'C+': 2.33, 'C': 2., 'C-': 1.67,
    'D+': 1.33, 'D': 1.,
    'F': 0.}

#Calculation variables
cumulativeCredits = 0
cumulativeGPA = 0
#Loop Control variables
currentLine = -1

for classLine in classList:
    classLine = classLine.replace('\n','')
    currentLine += 1
    classInfo = classLine.split(',')
    credits = 0
    grade = 0.0
    errors = {'cred': False, 'gpa': False, 'class': False}
    #Format Check
    try:
        credits = int(classInfo[0])
        if credits <= 0:
            errors['cred'] = True
    except:
        errors['cred'] = True
    if classInfo[1].upper() in gpaList:
        grade = gpaList[classInfo[1].upper()]
    else:
        errors['gpa'] = True
    if not re.search("[a-zA-Z]{3,5} ?[0-9]{3}", classInfo[2]): # Boasting my ability to use regex
        errors['class'] = True
    #Warn user and discard class if any errors (Except class name, which notifies problem but continues)
    if errors['cred'] and errors['gpa'] and errors['class']:
        print("Line " + str(currentLine) + ": Header Line. Discarding.")
        continue
    elif errors['cred']:
        print("!!ERROR   Line " + str(currentLine) + ": Credits was \"" + classInfo[0] + "\", which is not an integer at least 1. Discarding.")
        continue
    elif errors['gpa']:
        print("!!ERROR   Line " + str(currentLine) + ": Grade was \"" + classInfo[1] + "\", which is not a valid letter grade. Discarding.")
        continue
    elif errors['class']:
        print("!!WARNING Line " + str(currentLine) + ": Class name not formatted correctly. Continuing as normal.")
        # No continue statement
    #I would have the user prompts, but it isn't nessecary for the assignment and it's a lot of work, so I'm not doing it :)
    #Process if proper class
    print("Processing Class " + str(currentLine) + " (" + classInfo[2] + ")\n  Details: " + classInfo[0] + " Credits, Overall Grade " + classInfo[1] + " (" + str(grade) + ")")
    cumulativeGPA = cumulativeGPA + grade * credits
    cumulativeCredits = cumulativeCredits + credits
    
    
#calculate the GPA
finalGPA = str(round(cumulativeGPA/cumulativeCredits, 2))
print ('\nYour Final GPA is: ' + finalGPA + '\n')

# Edited in Notepad++, tested in PowerShell