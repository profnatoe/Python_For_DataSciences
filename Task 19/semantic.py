import spacy
#When 
#nlp = spacy.load('en') 
# the similarity output is different from the eb_core_web_md
#reason for this is because the model being used has no word vectors loaded 
# resulting in Doc.similarity method being based on the tagger, parse and NER, which may not give useful similarity judgement

nlp = spacy.load('en_core_web_md')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')


#Cat is similar to monkey because they are both animals
print(word1.similarity(word2))
#banana is not similar to monkey, one is a fruit the other an animal however a monkey eats banana 
print(word3.similarity(word2))
#hence the difference as compared to cat and banana. the similarity is lower in this case because cat don't eat banana
print(word3.similarity(word1))




tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


sentence_to_compare = 'Why is my cat on the car'

sentences = ['Where did my dog go',
'hello, where is my car',
'I\'ve lost my cat in my car',
'I\'d like my boat back',
'I will name my dog Diana']

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(str(sentence) +" - "+ str(similarity))
