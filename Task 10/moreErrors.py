x = float(input('Enter a number: '))
y = float(input('Enter a number: '))

#Runtime error: division by 0 => if a user enters y as 0
z = x/y

#Logical Error
average = x+y/2

print (x,'divided by',y,'equals: ',z)
print('average is: ', average)