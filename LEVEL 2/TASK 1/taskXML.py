import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

#prints out all child for movie
for movie in root.iter('movie'):
    print(movie.attrib)

counter = 1 

#Finds all the descriptions of movies and prints them out
all_descriptions = root.findall('.//description')

for description in all_descriptions:
  
    print(str(counter) + "".join(description.itertext()))
    counter = counter + 1

#
# Count Favorite and Non-Favorite Movies
# 

Favcount = 0
NFavcount = 0

#Find Movies that are favourites and  count them
for movie in root.findall(".genre/decade/movie[@favorite='True']"):
    Favcount = Favcount + 1

#Checks movies that are not favorite and stores the count to NFavcount
for movie in root.findall(".genre/decade/movie[@favorite='False']"):
    NFavcount = NFavcount + 1

print("\n\nNo. of Favorite Movies: ", str(Favcount))
print("No. of movies that are not favorite: ", str(NFavcount))