import spacy

gardenPathSentences = [
    "I know the words to that song about the queen don’t rhyme.",
    "That Jill is never here hurts.",
    "The horse raced past the barn fell.",
    "The florist sent the flowers was pleased.",
    "The raft floated down the river sank."
]



nlp = spacy.load("en_core_web_sm")
for doc in nlp.pipe(gardenPathSentences, disable=["tagger", "parser"]):
    #
    #tokenization
    tokens = [(token, token.orth_, token.orth) for token in doc]

    # Here we access the each token’s .orth_ method, which returns a string representation
    # of the token rather than a SpaCy token object, this might not always be desirable,
    # but worth noting. SpaCy recognises punctuation and is able to split these punctuation
    # tokens from word tokens. Many of SpaCy’s token method offer both string and integer
    # representations of processed text – methods with an underscore suffix return strings,
    # methods without an underscore suffix return integers. For example: 
    print(tokens)
    print("===================")
    #
    #Entity recognition
    print("Entity Recognition: \n", [(i, i.label_, i.label) for i in doc.ents])
    print("\n\n===================")


    #In the above sentences the entity recognition is able to detect the entities in the second sentence: 
    #meaning that it is able to tell that Jill is a person.
    #With all other remaining sentences it is not capable of doing the entity recognition as it returns an empty list.

