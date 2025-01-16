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

class Dzivnieks: 
    def __init__(self, vards, kajas): 
        self.vards = vards 
        self.kajas = kajas 
    def skanja(self): 
        print("random animal noise")
    def __str__(self):
        return f"{self.vards} un {self.kajas} kājas" 

#6.uzd ilze devās uz parīzi francijā. jābrauc uz lidostu 3/4 h; līdz lidojumam jāgaida 1 1/4 h; lidojums uz milānu 2 1/2 h - cik daudz laika dace pavadīja ceļā uz milānu

class Suns(Dzivnieks):
    def __init__(self, vards, kajas): 
        super().__init__(vards, kajas)
    def skanja(self):
        print("vau vau")

class Kakis(Dzivnieks):
    def __init__(self, vards, kajas): 
        super().__init__(vards, kajas)
    def skanja(self):
        print("mrrrrrr")

d1=Dzivnieks("Gauja",4)
print(d1)
d1.skanja()

d2=Suns("Bruno",9)
print(d2)
d2.skanja()

d3=Kakis("Fredis",12)
print(d3)
d3.skanja()
