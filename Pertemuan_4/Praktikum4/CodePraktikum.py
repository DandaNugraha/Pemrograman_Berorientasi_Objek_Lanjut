class Peneliti:
    def __init__(self, nama, institusi):
        self.nama = nama
        self.institusi = institusi
    
    def tulis_jurnal(self, judul):
        jurnal = Jurnal(judul)
        return jurnal
    
class Jurnal:
    def __init__(self, judul):
        self.judul = judul
        
peneliti1 = Peneliti("Andi", "LIPI")
peneliti1.tulis_jurnal = "Pengkajian Ilmu Pendidikan"
jurnal = Jurnal(peneliti1.tulis_jurnal)
print(jurnal.judul)

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    
    def gabung_kkm(self, nama_kkm):
        kkm = KelompokKKM(nama_kkm)
        return kkm
    
class KelompokKKM:
    def __init__(self, nama_kkm):
        self.nama_kkm = nama_kkm
        self.anggota = []
    
    def tambah_anggota(self, mahasiswa):
        self.anggota.append(mahasiswa)
        
mahasiswa1 = Mahasiswa("Danda", "2765")
mahasiswa2 = Mahasiswa("Dandi", "5672")
kkm1 = KelompokKKM("Panglima")
kkm1.tambah_anggota(mahasiswa1) 
kkm1.tambah_anggota(mahasiswa2) 
for m in kkm1.anggota:
    print(m.nama, m.nim)
print(kkm1.nama_kkm)

class Penulis:
    def __init__(self, nama):
        self.nama = nama
    
    def tulis_buku(self, judul):
        buku = Buku(judul, self)
        return buku
    
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

penulis = Penulis("John Doe")
buku = penulis.tulis_buku("My First Book")
print(f"Book title: {buku.judul}")
print(f"Author name: {buku.penulis.nama}")






