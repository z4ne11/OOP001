#2.uzd

class Autovaditajs:
    def __init__(self, vards = "", vecums = "", sodaPunkti = 0, numurzime = None):
        if numurzime is None:
            numurzime = []
        self.vards = vards
        self.vecums = vecums
        self.numurzime = numurzime
        self.sodaPunkti = sodaPunkti

    def numurzimeADD(self, jaunaNumurzime):
        self.numurzime.append(jaunaNumurzime)

    def sodaPunktiADD(self, jaunsSods):
        self.sodaPunkti += jaunsSods

    def izvade(self):
        self.numurzime = "\n".join(self.numurzime)
        print(f"\nVārds: {self.vards}, Vecums: {self.vecums};\nAutomašīnas īpašumā:\n{self.numurzime}\nSoda punkti: {self.sodaPunkti}")

A1 = Autovaditajs("Jurģis", "41")
A1.numurzimeADD("NL-1331")
A1.numurzimeADD("GR-34")
A1.numurzimeADD("14-TOU")
A1.numurzimeADD("1DEFTYU")
A1.sodaPunktiADD(4)
A1.izvade()

A1 = Autovaditajs("Samanta", "17")
A1.numurzimeADD("L123")
A1.numurzimeADD("XUIH")
A1.sodaPunktiADD(5)
A1.sodaPunktiADD(6)
A1.sodaPunktiADD(3)
A1.sodaPunktiADD(2)
A1.izvade()