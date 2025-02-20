# 2.uzd

class skolens():
    def __init__(self, vards = "", vecums = "" ,atzimes = None):
        if atzimes is None:
            atzimes = []
            self.vards = vards
            self.vecums = vecums
            self.atzimes = atzimes
            

    def ADDatzime(self, jaunaAtzime, summa = 0):
        self.atzimes.append(jaunaAtzime)
        #self.summa = summa
        #summa += int(jaunaAtzime)

    def izvade(self):
        atzimes = "\n".join(self.atzimes)
        print(f'Vārds: {self.vards}, Vecums: {self.vecums} gadi;\nAtzīmes:\n{atzimes}\n-\nVidēji: #N/A\n')
        

sk1 = skolens("Jurģis", "15")
sk1.ADDatzime("9")
sk1.ADDatzime("6")
sk1.ADDatzime("9")
sk1.ADDatzime("10")
sk1.izvade()

sk2 = skolens("Jana", "17")
sk2.ADDatzime("10")
sk2.ADDatzime("8")
sk2.ADDatzime("9")
sk2.ADDatzime("9")
sk2.izvade()