class Detail:
    def __init__(self):
        self.__id="<No Id>"
        self.__nama="<No Nama>"
        self.__kelamin="<No Kelamin>"
    def aturData(self,id,nama,kelamin):
        self.__id=id
        self.__nama=nama
        self.__kelamin=kelamin
    def tampilkanData(self):
        print("Id: ",self.__id)
        print("Nama: ", self.__nama)
        print("Kelamin: ", self.__kelamin)

class Pegawai(Detail): #Inheritance
    def __init__(self):
        self.__perusahaan="<No Perusahaan>"
        self.__dept="<No Dept>"
    def aturPegawai(self,id,nama,kelamin,perusahaan,dept):
        self.aturData(id,nama,kelamin)
        self.__perusahaan=perusahaan
        self.__dept=dept
    def tampilkanPegawai(self):
        self.tampilkanData()
        print("Perusahaan: ", self.__perusahaan)
        print("Departemen: ", self.__dept)

class Dokter(Detail): #Inheritance
    def __init__(self):
        self.__rumahSakit="<No Rumah Sakit>"
        self.__dept="<No Dept>"
    def aturPegawai(self,id,nama,kelamin,hos,dept):
        self.aturData(id,nama,kelamin)
        self.__rumahSakit=hos
        self.__dept=dept
    def tampilkanPegawai(self):
        self.tampilkanData()
        print("Rumah Sakit: ", self.__rumahSakit)
        print("Departemen: ", self.__dept)

def main():
    print("Pegawai Objek")
    e=Pegawai()
    e.aturPegawai(1,"Danda","Laki-laki","Sumber waras","THT")
    e.tampilkanPegawai()
    print("\nDokter Objek")
    d = Dokter()
    d.aturPegawai(2, "Gifani", "Perempuan", "Gunung Jati", "Mata")
    d.tampilkanPegawai()

if __name__=="__main__":
    main()