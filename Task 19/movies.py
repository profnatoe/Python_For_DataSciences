import spacy
nlp = spacy.load("en_core_web_md")

movies = []
similarities = []
msDictionary = {}

with open("movies.txt") as file_in:
    for line in file_in:
        movies.append(line)

sentence_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"

def NextMovie(description):
    print("Sentence to Compare with: \n=====\n")
    print(description)
    print("\n=============\n")
    model_sentences = nlp(description)
    for movie in movies:
        similarity = nlp(movie).similarity(model_sentences)
        similarities.append(similarity)
        
        msDictionary[similarity] = movie

    #print max similarity value just to compare with the dictionary : Debugging
    
    print("\nMax Similarity Value: \n", str(max(msDictionary)))
    print("\n\nMovie-Similarity Dictionary with Similarity as the Key:\n=====\n\n")
    for key,value in msDictionary.items():
        print(key, ' : ', value)

    return (msDictionary[max(similarities)])


print("================\n\nNext Movie to Watch is: ", NextMovie((sentence_to_compare)))
