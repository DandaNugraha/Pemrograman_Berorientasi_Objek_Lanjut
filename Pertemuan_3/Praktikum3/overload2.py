class Kotak:
    sisi = 5     
    def hitung_luas(self):
        return self.sisi * self.sisi

class Segitiga:
    alas = 5
    tinggi = 4
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

ktk = Kotak()
sgt = Segitiga()
print("Luas Kotak: ", ktk.hitung_luas())
print("Luas Segitiga: ", sgt.hitung_luas())