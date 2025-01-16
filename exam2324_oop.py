'''
class Doktorats():
    def __init__(self, nosaukums = "N/A", pacientuSk = 0): 
        self.nosaukums = nosaukums
        self.pacientuSk = pacientuSk
    def ievade(self):
        self.nosaukums = input('Ievadiet doktorāta nosaukumu: ') 
        try:
            self.pacientuSk = int(input('Ievadiet pacientu skaitu: '))
        except:
            self.pacientuSk = 0
        finally:
            print("Ievade veiksmīga: ", self.pacientuSk)
    def izvade(self):
        galotne = ""
        if (self.pacientuSk%10 !=1):
            galotne = "s"
        print(f"Doktorāts {self.nosaukums} apkalpo {self.pacientuSk} pacientu")


    
d1 = Doktorats()
d1.ievade()
d1.izvade()
'''

class Skolotajs:
    stunduSkNed = 0
    skolotajaTips = 0
    uzvards = "nezināms"

class SakumskolasSkolotajs(Skolotajs):
    klase = "x.i"
    def __init__(self):
        self.skolotajaTips=1
    def izvade(self):
        print(f"Sākumskolas (tips - {self.skolotajaTips}) skolotājs {self.uzvards}")

class VidusskolasSkolotajs(Skolotajs):
    pirmaisPrieksmets = "x priekšmets"
    otraisPrieksmets = "y priekšmets"
    abuPrieksmetuKopSk = 0

ss1 = SakumskolasSkolotajs()
ss1.izvade()