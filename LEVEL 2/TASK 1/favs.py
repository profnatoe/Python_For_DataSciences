import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()

Favcount = 0
for movie in root.findall(".genre/decade/movie[@favorite='True']"):
    print(movie.attrib)
    Favcount = Favcount + 1

print(Favcount)

