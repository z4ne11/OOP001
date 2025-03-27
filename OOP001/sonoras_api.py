'''

#1.uzdevums
import csv

#1.
with open('agenti.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        if row[0] == "Izglītības iestāde" or row[0] == "Valsts iestāde":
            print(",".join(row))

print("----------------------------------------")

#2.
with open('agenti.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        if "Rīga," in row[2]:
            print(",".join(row))

print("----------------------------------------")

#3.
with open('agenti.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    data = list(spamreader)
    dati = sorted(data, key=lambda x: x[2])
    for row in dati:
        print(",".join(row))

print("----------------------------------------")

'''

#2.uzdevums

import requests
import json

#1.

atbilde = requests.get("https://restcountries.com/v3.1/all")

#2.

print(atbilde.status_code)

if (atbilde.status_code!= 200):
    print("nav pareizi")

#3.

print(atbilde.text)
atbildeDict = json.loads(atbilde.text)
print(atbildeDict)
print(len(atbildeDict))

#print(atbildeDict[0]["name"].keys())

print(atbildeDict[0]["name"]["common"])
def visparpienemtie(atbildeDict):

    for i in atbildeDict:
        print(i["name"]["common"])

visparpienemtie(atbildeDict)

#4.

def valstuSk(atbildeDict):
    skaits = len(atbildeDict)
    print(f"Kopā ir dati par {skaits} valstīm")

valstuSk(atbildeDict)

#5.

def iedzivotajuSK(atbildeDict):
    kopejaisIedzSk = 0
    valstuSk = len(atbildeDict)

    for i in atbildeDict:
        #print(f'{i["name"]["common"]} pop:{i["population"]}')
        kopejaisIedzSk+=i["population"]
    vidSk = kopejaisIedzSk/valstuSk
    print(vidSk)

iedzivotajuSK(atbildeDict)

#6.

def valstisVisvairakIedz(atbildeDict):
    sak = sorted(atbildeDict, key = lambda elem:elem["population"])
    print("Visvairāk ir:")
    print(sak[-1]["name"]["common"])
    print(sak[-1]["population"])

valstisVisvairakIedz(atbildeDict)

#7.