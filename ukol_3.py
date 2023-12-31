import json


with open ("body.json", mode="r", encoding="utf-8") as slozka:
    studenti = json.load(slozka)
print(studenti)

prospech = {}

for jmeno, znamka in studenti.items():
    if int(znamka) < 60:
        prospech[jmeno] = "Fail" 
    else:
        prospech[jmeno] = "Pass"    
print(prospech)

with open ("prospech.json", mode= "w", encoding="utf-8") as slozka2:
    json.dump(prospech, slozka2, ensure_ascii = False)
print(prospech)