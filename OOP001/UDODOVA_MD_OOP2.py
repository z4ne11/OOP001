class augi():
       def __init__(self, nosaukums = "", daudzums = ""):
        self.nosaukums = nosaukums
        self.daudzums = daudzums

        def __str__(self):
            return f"{self.nosaukums}, {self.daudzums} grami/n"
        
class augli(augi):
    def __init__(self, nosaukums = "", daudzums = "", seklas = ""):
