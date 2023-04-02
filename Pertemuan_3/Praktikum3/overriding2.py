from math import pi


class Bangun:
    def __init__(self, nama):
        self.nama = nama

    def luas(self):
        pass

    def fakta(self):
        return "Aku bangun 2D."

    def __str__(self):
        return self.nama


class Kotak(Bangun):
    def __init__(self, panjang):
        super().__init__("Kotak")
        self.panjang = panjang

    def luas(self):
        return self.panjang**2

    def fakta(self):
        return "Setiap sisi kotak memiliki sisi miring 90°."


class Bulat(Bangun):
    def __init__(self, radius):
        super().__init__("Bulat")
        self.radius = radius

    def luas(self):
        return pi*self.radius**2


a = Kotak(4)
b = Bulat(7)
print(b)
print(b.fakta())
print(a.fakta())
print(b.luas())
