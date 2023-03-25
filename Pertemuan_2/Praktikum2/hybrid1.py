class Kendaraan:
    def info_kendaraan(self):
        print("Didalam class Kendaraan")

class Mobil(Kendaraan):
    def info_mobil(self):
        print("Didalam class Mobil")

class Truk(Kendaraan):
    def info_truk(self):
        print("Didalam class Truk")

class MobilSport(Mobil, Kendaraan):
    def info_mobil_sport(self):
        print("Didalam class MobilSport")

s_car = MobilSport()

s_car.info_kendaraan()
s_car.info_mobil()
s_car.info_mobil_sport()