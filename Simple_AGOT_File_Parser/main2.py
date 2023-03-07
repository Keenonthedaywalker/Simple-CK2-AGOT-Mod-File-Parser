import re

with open("Essos.txt", "r", encoding="ISO-8859-1") as f:
    s = f.read()
    print(s)

result = re.findall('name[ ]*=[ ]*"([A-z ]+)"\n[ ]+culture[ ]*=[ ]*([A-z]+)', str(s))

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
        
print(names_by_culture)
with open("text.txt", "w", encoding="utf8") as outfile:
    outfile.write(s)