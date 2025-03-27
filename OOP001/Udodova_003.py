#3.uzd
from abc import ABC

class Telpa():
    
    def __init__(self, telpasNr = "", platiba = 0 , cilvekuSk = 0):
        self.telpasNr = telpasNr
        self.platiba = platiba
        self.cilvekuSk = cilvekuSk
    def cilvekuSkADD(self, cilvekiPievienojas):
        self.cilvekuSk += cilvekiPievienojas
    

class Datorklase(Telpa):
    def __init__(self, telpasNr = "", platiba = 0 , cilvekuSk = 0, datori = 0):
        super().__init__(telpasNr = "", platiba = 0 , cilvekuSk = 0)
        self.telpasNr = telpasNr
        self.platiba = platiba
        self.cilvekuSk = cilvekuSk
        self.datori = datori
        if self.cilvekuSk > self.datori:
            self.zinojums1 = "; nepieciešami papildus datori"
        else:
            self.zinojums1 = ""
 
        if self.cilvekuSk*0.8> self.platiba:
            self.zinojums2 = "; pārāk daudz cilvēku"
        else:
            self.zinojums2 = ""

    def __str__(self):
        return(f'Datorklase {self.telpasNr}, {self.platiba}kvm, {self.datori} datori, {self.cilvekuSk} cilvēki{self.zinojums1}{self.zinojums2}')


class Kabinets(Telpa):
    def __init__(self, telpasNr = "", platiba = 0 , cilvekuSk = 0, galduSk = 0):
        super().__init__(telpasNr = "", platiba = 0 , cilvekuSk = 0)
        self.telpasNr = telpasNr
        self.platiba = platiba
        self.cilvekuSk = cilvekuSk
        self.galduSk = galduSk
        if self.cilvekuSk > self.galduSk:
            self.zinojums3 = "; nepieciešami papildus galdi"
        else:
            self.zinojums3 = ""
 
        if self.cilvekuSk > self.platiba:
            self.zinojums4 = "; pārāk daudz cilvēku"
        else:
            self.zinojums4 = ""

    def __str__(self):
        return(f'Kabinets {self.telpasNr}, {self.platiba}kvm, {self.galduSk} galdi, {self.cilvekuSk} cilvēki{self.zinojums3}{self.zinojums4}')


telpa1 = Datorklase("34", 12, 20, 16)
telpa1.cilvekuSkADD(10)
print(telpa1)
telpa2 = Datorklase("14", 12, 13, 10)
print(telpa2)
telpa3 = Datorklase("25", 15, 16, 20)
print(telpa3)

print("\n")

telpa4 = Kabinets("13", 12, 20, 16)
print(telpa4)
telpa5 = Kabinets("11", 12, 10, 10)
print(telpa5)
telpa6 = Kabinets("5", 16, 16, 10)
print(telpa6)