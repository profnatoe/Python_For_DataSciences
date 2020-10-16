
def daysofWeek():
    return  ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(daysofWeek())

def replaceFunc(sentence):
    wordlist = sentence.split()
    wordlist[1] = "Hello"
    
    return " ".join(wordlist)

print(replaceFunc("World, It, I am Here to warn you"))