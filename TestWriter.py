import random
import os

"""
OUTPUT_PATH = "pyOutput/"
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)
f = open(OUTPUT_PATH + "TestTextFile.txt", 'w')
f.write("Number result: " + str(random.randrange(50)))
f.close()
f = open(OUTPUT_PATH + "TestTextFile.txt", 'r')
print(f.read())
f.close()
"""

# Actual class stuff
PROJECT_FILE_PATH = "example.txt"

if not os.path.exists(PROJECT_FILE_PATH):
    print("File \"" + PROJECT_FILE_PATH + "\" doesn't exist!")
    quit()
openFile = open(PROJECT_FILE_PATH, 'r')
print(openFile.read())
openFile.close()
