class turnirs():
    def __init__ (self, nosaukums = "", cilvSkaits = "", grupuSkaits = "", sports = "", sponsori = None):
         if sponsori is None:
            sponsori = []
            self.nosaukums = nosaukums
            self.cilvSkaits = cilvSkaits
            self.grupuSkaits = grupuSkaits
            self.sports = sports
            self.sponsori = sponsori

    def sponsorsADD(self, NEWsponsors):
        self.sponsori.append(NEWsponsors)

    def izvade(self):
        sponsori = "\n".join(self.sponsori)
        print(f'Šis ir {self.sports} turnīrs "{self.nosaukums}", kurā piedalās {self.cilvSkaits} cilvēki, {self.grupuSkaits} grupās. \nSponsori:\n{sponsori}\n')
        

turnirs1 = turnirs("Last Dab 2025", "18", "5", "Tortnite")
turnirs1.sponsorsADD("Adidaš")
turnirs1.sponsorsADD("Mike")
turnirs1.sponsorsADD("DolčeNKabana")


turnirs2 = turnirs("2025", "66", "11", "Volleyball")
turnirs2.sponsorsADD("Samsungs")
turnirs2.sponsorsADD("Ventspils osta")
turnirs2.sponsorsADD("Dior")

turnirs1.izvade()
turnirs2.izvade()

print("esmu te")
