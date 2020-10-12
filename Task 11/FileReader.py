namecounter = 1
datecounter = 1
namelist = []
birthlist = []

with open('dob.txt') as name:
    for row in name:
        rowstrings = row.split()
        names = rowstrings[0] + " " + rowstrings[1]
        birthdate = rowstrings[2] + " " + rowstrings[3] + " " + rowstrings[4]
        namelist.append(names)
        birthlist.append(birthdate)
print("\nNames: \n\n")
for row in namelist:
    print(str(namecounter) + ". " + row)
    namecounter += 1
print("\n\nBirth Dates: \n\n")

for row in birthlist:
    print(str(datecounter) + ". " + row)
    datecounter += 1