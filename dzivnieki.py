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
    def init(self, vards, kajas): 
        self.vards = vards 
        self.kajas = kajas 
    def skanja(self): 
        print("random animal noise")

#6.uzd ilze devās uz parīzi francijā. jābrauc uz lidostu 3/4 h; līdz lidojumam jāgaida 1 1/4 h; lidojums uz milānu 2 1/2 h - cik daudz laika dace pavadīja ceļā uz milānu

d1=Dzivnieks("Gauja",4)
d1.skanja()

class Suns(Dzivnieks):
    def init(self, vards, kajas): 
        super().__init__(vards, kajas)
    def skanja(self):
        print("vau vau")