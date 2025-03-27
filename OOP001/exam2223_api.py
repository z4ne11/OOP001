import requests
import json

#1.uzd 
atbilde = requests.get("https://data.gov.lv/dati/lv/api/3/action/datastore_search?resource_id=92ac6e57-c5a5-444e-aaca-ae90c120cc3d&limit=100000000000000000000000000000000000000000000000000")


#print(atbilde.text)
print(atbilde.status_code)
if (atbilde.status_code!= 200):
    print("nav pareizi")

dati = json.loads(atbilde.text)
ieraksti = dati["result"]["records"]

print("Baterijas un akumulatorus iespējams nodot:")
for i in ieraksti:
    if i["8 : Baterijas un akumulatori"].lower()== "x":
        print(i["pilsetanovads"], i["adrese"])
print("---------------------------------------------")

print("Nolietotās riepas iespējams nodot:")
for i in ieraksti:
    if i["10 : Nolietotās riepas"].lower()== "x":
        print(i["pilsetanovads"], i["adrese"])
print("---------------------------------------------")

'''print("Metālu iespējams nodot:")
for i in ieraksti:
    if i["3 : Metāls"].lower()== "x":
        print(i["pilsetanovads"], i["adrese"])
print("----------------------------------------------")'''

#2.uzd