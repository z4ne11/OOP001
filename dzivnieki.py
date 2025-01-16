#github cat - izveido failu 
# #github echo - ielikt kko iekšā 
# #github echo "print(3+4)" >> dzivnieki.py pieliek failā klat 
# #github echo "print(3+4)" > dzivnieki.py aizvieto faila saturu

#github izveido repository(mape) "nosaukums"
#copy HTTPS linku
#mapē atver gitbash
#git clone links
#git add . 
#git commit -m"komentars"
#git push origin

from abc import abstractmethod

class Dzivnieks(): 
    def __init__(self, vards, kajas): 
        self.vards = vards 
        self.kajas = kajas 
    @abstractmethod #norāda ka nākamā metode būs abstrakta un ja ir abstrakts tad nevar uztaisīt konkrētu objektu
    def skanja(self): 
        print("random animal noise")
    def __str__(self):
        return f"{self.vards} un {self.kajas} kājas" 

#6.uzd ilze devās uz parīzi francijā. jābrauc uz lidostu 3/4 h; līdz lidojumam jāgaida 1 1/4 h; lidojums uz milānu 2 1/2 h - cik daudz laika dace pavadīja ceļā uz milānu

class Suns(Dzivnieks):
    def __init__(self, vards, kajas): 
        super().__init__(vards, kajas)
        self.vards = "Sunītis "+self.vards
    def skanja(self):
        print("vau vau")

class Kakis(Dzivnieks):
    def __init__(self, vards, kajas): 
        super().__init__(vards, kajas)
        self.vards = "Minkāns "+self.vards
    def skanja(self):
        print("mrrrrrr")

class Govs(Dzivnieks):
    def skanja(self):
        print("muuuuuuuuuuuuu")

d1=Govs("Gauja",4)
print(d1)
d1.skanja()

d2=Suns("Bruno",4)
print(d2)
d2.skanja()

d3=Kakis("Fredis",4)
print(d3)
d3.skanja()

dzivniekuSaraksts = []
dzivniekuSaraksts.append(Suns("Bruno", 4))
dzivniekuSaraksts.append(Suns("Šeila", 4))
dzivniekuSaraksts.append(Suns("Pepa", 4))
dzivniekuSaraksts.append(Suns("Riko", 4))
dzivniekuSaraksts.append(Kakis("Fredis", 4))
dzivniekuSaraksts.append(Kakis("Rūdis", 4))
dzivniekuSaraksts.append(Kakis("Muris", 4))
dzivniekuSaraksts.append(Govs("Gauja", 4))
dzivniekuSaraksts.append(Govs("Roja", 4))

print("#################################")
for dzivnieks in dzivniekuSaraksts:
    print (dzivnieks)
    dzivnieks.skanja()