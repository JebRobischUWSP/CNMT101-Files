username = 'xXx_Sn1p3rBl4d3S1gm4W0lf_xXx'
password = 'password123wow'
invalidSymbols = ['!',' ']

print(len(username), len(password))

if len(password) < 10:
    print('Password too short!')
else:
    print('Password length okay')
for symbol in invalidSymbols:
    if symbol in password:
        print("You can't use [" + symbol + "]")
    else:
        print("Check for [" + symbol + "] passed")
