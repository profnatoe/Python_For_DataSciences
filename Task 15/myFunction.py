
def daysofWeek():
    return  ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(daysofWeek())

def sentenceReplace(sentence):

    hello = " ".join(["{} hello".format(word) for idx, word in enumerate(sentence.split())
    if idx % 2 == 0])   
    print("==========\n\nModified Sentence: \n\n", hello)

sentence = "What in the world are you doing on these python thorny land"
print("Original Sentence: ", sentence)
sentenceReplace(sentence)