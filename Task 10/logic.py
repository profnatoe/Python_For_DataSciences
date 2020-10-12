x = float(input('Enter a number: '))
y = float(input('Enter a number: '))

#Since in mathematics we follow BODMAS Rule the following will give us a wrong
#answer as it will start by dividing y by 2 instead of dividing (x + y) by 2
z = x+y/2
print ('The average of the two numbers you have entered is:',z)