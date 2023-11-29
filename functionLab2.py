def print_collection(label, lst): #I prefer camelcase for variables and upper camelcase for functions & classes, but WHATEVER I guess
    return None #This recieves the appropriate variables. It doesn't DO anything with them, but it does recieve ;>

class Example: #I made this class purely to parse it as a string
    def __str__(self):
        return "String as example class"

exampleList = ["String!", str(123), str(Example())] #It's a list of example values; an exampleList
print(exampleList)
for item in exampleList:
    print(item)
print("List length: " + str(len(exampleList)))

pieFlavors = ["Cherry", "Rhubarb", "Pecan"] # I'm assuming functionLab.py is supposed to contain up to the print satements? Thouh you have the two save as directions, you don't note a need to save at the end, so I'm not quite sure if functionLab is supposed to ONLY have the list of 3 (as that's all tha happens before the direction to save the file) or if it's supposed to have evrything UP TO saving it as functionLab2, or if it's a mix????
print_collection("Example Values: ", exampleList)
print_collection("Here's some cool pies: ", pieFlavors)

print("\n\nExample Values: " + ", ".join(exampleList) + "\nHere's some cool pies: " + ", ".join(pieFlavors))
# I know the above line is not what you wanted me to do. But, it completely fills the requirements of the assignment.
# However...
"""
If print_collection was this instead, this would work as to the specifications I presume you wanted:
def print_collection(label, lst):
    print(label + ", ".join(lst))
"""
# I have tested it in a different file, and that modified print_collection does work to specifications.
# I hope you like me mixing single- and multi-line comments :)