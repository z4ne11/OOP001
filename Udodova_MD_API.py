import json
import requests
from collections import defaultdict

# visas augstskolas Latvijā 
skaits = 0
augstskolasLV = requests.get('http://universities.hipolabs.com/search?country=Latvia')
augstskolasLVsaraksts = json.loads(augstskolasLV.text)
print("Latvijā ir", len(augstskolasLVsaraksts), "augstkolas:")

for augstskolasLVprint in augstskolasLVsaraksts:
    print("\t",augstskolasLVprint["name"])

# visas augstskolas Francijā
augstskolasFR = requests.get('http://universities.hipolabs.com/search?country=France')
augstskolasFRsaraksts = json.loads(augstskolasFR.text)
print("Francijā ir", len(augstskolasFRsaraksts), "augstkolas.")

#eu
EUsk=0
for eu in augstskolasFRsaraksts:
    if any(".eu/" in majaslapa for majaslapa in eu["web_pages"]):
        EUsk+=1
print("No visām Francijas augstskolām ",round(EUsk / len(augstskolasFRsaraksts) * 100, 2),"procenti ir mjas lapas ar eu domēnu")

#paris
augstskolasFR2 = requests.get('http://universities.hipolabs.com/search?country=France&name=Paris')
augstskolasFRsaraksts2 = json.loads(augstskolasFR2.text)
print("Francijā ir", len(augstskolasFRsaraksts2), "augstkolas, kuru nosaukumi satur Paris.")

# visas augstskolas
skolas = requests.get('http://universities.hipolabs.com/search?name=School')
SKOLASsaraksts = json.loads(skolas.text)
print("Kopumā ir", len(SKOLASsaraksts), "augstskolas, kuru nosaukumi satur School.")

#https Francijā
HTTPSsk=0
for https in augstskolasFRsaraksts:
    if any("https" in majaslapa for majaslapa in https["web_pages"]):
        HTTPSsk+=1
print("Francijā ir", round(HTTPSsk / len(augstskolasFRsaraksts) * 100, 2),"procenti mājaslapas, kuras sākas ar https.")


# 8. punkts
EiropasValstis = [
    "Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium",
    "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark",
    "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland",
    "Ireland", "Italy", "Kazakhstan", "Kosovo", "Latvia", "Liechtenstein", "Lithuania",
    "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia",
    "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia",
    "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"
]

augstskolu_skaits = defaultdict(int)
for valsts in EiropasValstis:
    konkretaValsts = requests.get(f'http://universities.hipolabs.com/search?country={valsts}')
    augstskolas = konkretaValsts.json()
    augstskolu_skaits[valsts] = len(augstskolas)

max_valsts = max(augstskolu_skaits, key=augstskolu_skaits.get)
print(f"Valsts ar visvairāk augstskolām ir {max_valsts}.")
