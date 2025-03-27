#2.uzd
import json
import requests

dati = requests.get('https://restcountries.com/v3.1/all')

#/country=
sarakstsVALSTIS = json.loads(dati.text)
print("pieejama informācija par", len(sarakstsVALSTIS), "valstīm")

dati2 = json.loads(dati.text)

UNsk = 0
for i in dati2:
    if i["unMember"]== True:
        UNsk= UNsk +1
print(UNsk, "valstis no šī saraksta ir Apvienoto Nāciju Organizācijā (United Nations)")

WEEKstart = 0
for i in dati2:
    if i["startOfWeek"]== "monday":
        WEEKstart= WEEKstart +1
print(round(WEEKstart / len(sarakstsVALSTIS) * 100, 2), "% valstis no šī saraksta nedēļu sāk ar pirmdienu")


RepublicSK = 0
for nosaukums in dati2:
     if "Republic"in nosaukums["name"]["official"]:
        RepublicSK= RepublicSK +1
print(RepublicSK, "valstu oficiālajos nosaukumos angļu valodā ir vārds Republika (Republic)")

iedzivotajuSK = 0
for i in dati2:
    if i["region"]== "Europe":
        if i["landlocked"]== True:
            valstsSK = i["population"]
            iedzivotajuSK = iedzivotajuSK + valstsSK
print(iedzivotajuSK, "ir kopējais iedzīvotāju skaits visās valstīs Eiropā, kurām ir tikai sauszemes robeža")



