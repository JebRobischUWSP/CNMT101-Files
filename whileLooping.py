'''
userNumber = -1
print('need good number')
while(True):
    userNumber = input('give number ')
    try:
        if int(userNumber) >= 0:
            break
    except:
        _ = None #Except has to have executed content to work
    print('wrong number. bad number.')
print('good job!')
'''
isInteger = False;

while not isInteger:
    userInput = input('Please enter an integer: ');

    # Convert to integer
    try:
        convertInt = int(userInput);
        print('This is an integer: ' + userInput);
        isInteger = True;
    except:
        print('This (' + userInput + ') is not an integer');
