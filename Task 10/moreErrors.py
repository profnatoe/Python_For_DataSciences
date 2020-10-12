x = float(input('Enter a number: '))
y = float(input('Enter a number: '))

#Runtime error: division by 0 => if a user enters y as 0
z = x/y

#Compilation error(s)
if y==0
    print(y, 'y is 0')
    else print('y is not equal to 0')
        
#Logical Error
average = x+y/2

print (x,'divided by',y,'equals: ',z)
print('average is: ', average)