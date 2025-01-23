class csdd():
    def __init__(self, nosaukums = "unknown ", cilvekuSkaits = "unknown ", grupuSkaits = "unknown ", masa = "unknown ", degviela = "unknown "):
        self.nosaukums = nosaukums
        self.cilvekuSkaits = cilvekuSkaits
        self.datums = datums
        self.masa = masa
        self.degviela = degviela
    def __str__(self):
        return f"zīmols: {self.zimols} \nmodelis: {self.modelis} \nreģistrācijas datums: {self.datums} \npilna masa: {self.masa} \ndegvielas veids: {self.degviela}" 

masina=csdd("Audi","A4", "22.10.20219", 1800, "BG")
print(masina)

Turnīra nosaukums
Cilvēku skaits
Grupu skaits
Sporta veids
Sponsoru saraksts