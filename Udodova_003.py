# 3.uzd
import math

class geometry():
    def __init__(self, krasa = "", c_x = 0, c_y = 0):
        self.krasa = krasa
        self.c_x = c_x
        self.c_y = c_y
class kvadrats(geometry):
    def __init__(self, krasa = "", c_x = 0, c_y = 0, malasGarums = 0):
        super.__init__(krasa, c_x = 0, c_y = 0)
        self.malasGarums = malasGarums
        self.laukums = malasGarums*malasGarums
        self.perimetrs = 4 * malasGarums
    def __str__(self):
        return(f'Kvardāts ({self.c_x},{self.c_y}), mala = {self.malasGarums}, laukums = {self.laukums}, perimetrs = {self.perimetrs}')



class aplis(geometry):
    def __init__(self, krasa = "", c_x = 0, c_y = 0, radiuss = 0):
        super.__init__(krasa, c_x = 0, c_y = 0)
        self.radiuss = radiuss
        self.laukums = math.pi*self.radiuss**2
        self.perimetrs = math.pi*2*self.radiuss
    def __str__(self):
        return(f'Aplis ({self.c_x},{self.c_y}), rādiuss = {self.malasGarums}, laukums = {self.laukums}, perimetrs = {self.perimetrs}')


figura1 = kvadrats("Melna", 3.0, 40, 3.433)
print(figura1)
figura2 = kvadrats("Melna", 30, 4.0, 7)
print(figura2)
figura3 = kvadrats("Melna", 0, 10, 8)
print(figura3)

figura4 = aplis("Rozā", 3.0, 40, 3.433)
print(figura4)
figura5 = aplis("Rozā", 30, 4.0, 7)
print(figura5)
figura6 = aplis("Rozā", 0, 4.0, 8)
print(figura6)