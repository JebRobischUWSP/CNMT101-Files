class Example:
    def __repr__(self):
        return "Example()"
    def __str__(self):
        return "You Printed an instance of 'Example'"
exampleList = ["String!", 123, Example()]
print(exampleList) #Interesting: printing a list calls on __repr__, though printing individually calls on __str__ (the latter being expected from a print() call) 
for item in exampleList:
    print(item)
print("List length: " + str(len(exampleList)))
