class Kendaraan:
    def __init__(self, brand, model, harga):
        self.brand = brand
        self.model = model
        self.harga = harga

    def show(self):
        print('Detail:', self.brand, self.model, 'Harga:', self.harga)

    def kecepatan_max(self):
        print('Kecepatan max mobil ini 160km/jam')

    def sistem_gigi(self):
        print('Kendaraan ini memiliki 6 gigi')

class Mobil(Kendaraan):
    def kecepatan_max(self):
        print('Kecepatan max mobil ini 260km/jam')

    def sistem_gigi(self):
        print('Mobil ini memiliki sistem gigi otomatis')

mobil = Mobil('Audi', 'R8', 9000000)
mobil.show()

mobil.kecepatan_max()
mobil.sistem_gigi()

kendaraan = Kendaraan('Nissan', 'Magnite', 550000)
kendaraan.show()

kendaraan.kecepatan_max()
kendaraan.sistem_gigi()
