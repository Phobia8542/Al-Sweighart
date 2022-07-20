#lesson 11
#def div42by(divideBy):
    #try:
        #return 42 / divideBy
    #except ZeroDivisionError:
        #print ('Error: You tried to divide by zero.')

#print(div42by(2))
#print(div42by(12))
#print(div42by(0))
#0 can not be processed; cancels the order and 1 will never display
#print(div42by(1))

#Come back to allow for multiple attempts
print ('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print ('That is a lot of cats.')
    else:
        print ('That is not that many cats.')
except ValueError:
    print('You did not enter a number')
#Figure out how to account for negative numbers
#Come back when you can represent a str value as an integer without getting an error message.