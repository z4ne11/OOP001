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
    def ievade(self):
        self.uzvards = input("Ievadiet sākumskolas skolotāja uzvārdu: ")
        self.klase = input("Ievadiet skolotāja klasi: ")
        self.stunduSkNed = input("Ievadiet skolotāja stundu skaitu: ")
    def izvade(self):
        print(f"Sākumskolas (tips - {self.skolotajaTips}) skolotājs {self.uzvards} māca {self.stunduSkNed} stundas {self.klase} klasē.")

class VidusskolasSkolotajs(Skolotajs):
    def __init__(self):
        self.skolotajaTips=3
    pirmaisPrieksmets = "x priekšmets"
    otraisPrieksmets = "y priekšmets"
    pirmaisPrieksmetsStundas = 0
    otraisPrieksmetsStundas = 0
    stunduSkNedela = 0
    def ievade(self):
        self.uzvards = input("Ievadiet vidusskolas skolotāja uzvārdu: ")
        self.pirmaisPrieksmets = input("Ievadiet pirmo pasniegto priekšmetu: ")
        self.pirmaisPrieksmetsStundas = input("Ievadiet priekšmeta stundu skaitu: ")
        self.otraisPrieksmets = input("Ievadiet otro pasniegto priekšmetu: ")
        self.otraisPrieksmetsStundas = input("Ievadiet priekšmeta stundu skaitu: ")
    def cikStundasKopa(self):
        self.stunduSkNedela = self.pirmaisPrieksmetsStundas + self.otraisPrieksmetsStundas
    def izvade(self):
        print(f"Vidusskolas (tips - {self.skolotajaTips}) skolotājs {self.uzvards} māca šādus priekšmetus: {self.pirmaisPrieksmets} un {self.otraisPrieksmets} kopā {self.stunduSkNedela} stundas")




ss1 = SakumskolasSkolotajs()
ss1.ievade()
ss1.izvade()

vs1 = VidusskolasSkolotajs()
vs1.ievade()
vs1.izvade()

