#1.uzd
#Name,Type,HP,Attack,Defense,Speed
import csv
saraksts = []

with open('Udodova_pokemon_data.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for rinda in spamreader:
        saraksts.append(rinda)
       
saraksts2 = sorted(saraksts, key = lambda x: x[3])
print("vislielākais attack ir", saraksts2[-1][0])

saraksts3 = sorted(saraksts, key = lambda x: x[5])
print("vislielakais ātrums ir", saraksts3[1][0])

sk = 0
for tips in saraksts:
    if tips[1] == "Water":
        sk +=1
print("ūdens tipa pokemoni ir", sk)

saraksts4 = sorted(saraksts, key = lambda x: x[4])

