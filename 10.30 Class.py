h = 11;
hFloat = 11.0;
if h < 11:
    print('Huh?');

if h <= 11:
    print('Correct!');

if h:
    print('More than just booleans!*');

if h != '11':
    print('Also not a string!');

if str(h) == '11':
    print(' ...but now it is!')

if h == hFloat:
    print('11 == 11.0 (Equivalence)');

if not (h == hFloat and type(h) == type(hFloat)):
    print('11 !== 11.0 (Strict Equivalence)');
'''
if a > 1:
    print('I like tacos!')
'''
