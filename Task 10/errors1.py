# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print "Welcome to the error program"
    print "\n"

    ageStr == "24 years old" #I'm 24 years old.
    age = int(ageStr)
    print("I'm"+age+"years old.")
    three = "3"

    answerYears = age + three

print "The total number of years:" + "answerYears"
answerMonths = answer*12
print "In 3 years and 6 months, I'll be " + answerMonths + " months old"

#HINT, 330 months is the correct answer

#Corrected

# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

#Fixed an Error: Compilation Error
print("Welcome to the error program")
#Fixed an Error: Compilation Error
print("\n")

#Fixed an Error: Compilation Error
ageStr = "24"
age = int(ageStr)
#Fixed an Error: Compilation Error
print("I'm " + str(age) + "years old.")
three = "3"

#Fixed an Error: Compilation Error
answerYears = str(age) + three

print("The total number of years:" + ageStr)
#Fixed an Error: Compilation
answerMonths = int(ageStr)*12
print("In 3 years and 6 months, I'll be " + str(answerMonths+ (3*12+6)) + " months old")

#HINT, 330 months is the correct answer