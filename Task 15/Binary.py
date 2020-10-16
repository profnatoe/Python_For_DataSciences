import math
#binary input from a user: console
binary_string = input("Enter a binary number :")

#tries to convert 
try:
    decimal = int(binary_string,2)  
    print("The decimal value is :", decimal)    
#prints out a message if the above fails    
except ValueError:
    print("Invalid binary number")