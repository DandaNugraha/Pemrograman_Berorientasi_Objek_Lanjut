class Kendaraan:
    def __init__(self, tarif):
        self.tarif = tarif
    def __lt__(self, lainnya):
        return self.tarif < lainnya.tarif

bus= Kendaraan(10)
mobil= Kendaraan(30)
bandingkan= bus < mobil
print(bandingkan)