with open('input.txt') as infile:
    words = 0
    characters = 0
    numVowl = 0
    for lineno, line in enumerate(infile, 1):
        wordslist = line.split()
        words += len(wordslist)
        characters += sum(len(word) for word in wordslist)
        for char in line.lower():
            if char in 'aeiou':
                numVowl += 1

print("No. of line(s): ", lineno)
print("No. of word(s): ", words)
print("No. of char(s): ", characters)
print("No. of vowels : ", numVowl)