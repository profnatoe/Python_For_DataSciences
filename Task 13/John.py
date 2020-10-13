incorrect_names = []

while True:
    name = input("Enter your name: \n")
    if name == "John":
        break
    incorrect_names.append(name)

print("Incorrect names", incorrect_names)