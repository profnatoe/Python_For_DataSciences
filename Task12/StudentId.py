students = int(input("Please enter the amount of students registered: "))
id_number = ""

for a in range (0, students):
    id_number = (int(input("Please enter student ID numbers: ")))
    id_number = id_number + 1
    with open('reg_form.txt', 'a') as file:
        file.write("\n"+ str(a+1) + ". Student ID number: " + str(id_number))

print ("Thank you, ID numbers saved to txt file reg_form")