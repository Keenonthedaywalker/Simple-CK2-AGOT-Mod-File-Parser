import re

# Make sure to add a space and a symbol in the dynasty part of the text file so
# that commas and quotes are generared correctly.
with open("test.txt", "r", encoding="ISO-8859-1") as f:
    s = f.read()
    print(s)

result = re.findall('name[ ]*=[ ]*"([A-z ]+)"\n[ ]+culture[ ]*=[ ]*([A-z]+)', s)

names_by_culture = {}
for i in result:
    name = i[0]
    culture = i[1] 
    try:
        names_by_culture[culture].append(name)
    except:
        names_by_culture[culture] = []
        names_by_culture[culture].append(name)
        
print(names_by_culture)