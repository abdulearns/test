# a=50

# if a>50:
#     print('yes')
# elif a<50:
#     print("hemine")  
# else:
#     print('nadarimo')


###########################################################################
# Program which takes a number as input and evaluates if it's even or odd #
###########################################################################

# Adding exception handling
try:
    r = int(input('Please enter a number: '))
except:
    print('Invalid input. Not a number..')
else:
    if r%2 == 0:
        print('{} is even' .format(r))
    else:
        print('{} is fard' .format(r))
