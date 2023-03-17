#Contoh 1:
class Mobil:     
    def __init__(self, merk, warna, roda): 
        self.merk = merk
        self.warna = warna
        self.roda = roda

    def info(self): 
        print(f"Mobil {self.merk} berwarna {self.warna} beroda {self.roda}")

mobilA = Mobil("Toyota", "Hitam", "4")
mobilA.info() # Output: Mobil Toyota berwarna Hitam 

#Contoh 2: 
class Mahasiswa:     
    def __init__(self, nama, npm, kelamin): 
        self.nama = nama
        self.npm = npm
        self.kelamin = kelamin

    def info(self): 
        print(f"Nama: {self.nama}\nNPM: {self.npm}\nKelamin: {self.kelamin}") 

mahasiswaB = Mahasiswa("Ahmad", "123456789", "Laki-laki") 
mahasiswaB.info() 

#Contoh 3:
class Lingkaran:     
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari 

    def luas(self): 
        return 3.14 * (self.jari_jari ** 2)

lingkaranA = Lingkaran(7)
print(f"Jari-jari lingkaranA (7), maka luas lingkaran: {lingkaranA.luas()}")
lingkaranB = Lingkaran(8)
print(f"Jari-jari lingkaranB (8), maka luas lingkaran: {lingkaranB.luas()}")

#Contoh 4: 
class Buku:     
    def __init__(self, judul, penulis, penerbit): 
        self.judul = judul
        self.penulis = penulis 
        self.penerbit = penerbit

    def info(self): 
        print(f"Judul: {self.judul}\nPenulis: {self.penulis}\nPenerbit: {self.penerbit}") 
    
bukuA = Buku("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "The Books")
bukuA.info() 

#Contoh 5: 
class PesawatTerbang: 
    def __init__(self, maskapai, tujuan, jenisPesawat): 
       self.maskapai = maskapai
       self.tujuan = tujuan
       self.jenisPesawat = jenisPesawat

    def info(self): 
       print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}\nJenis Pesawat: {self.jenisPesawat}")
       
pesawatA = PesawatTerbang("Garuda Indonesia", "Jakarta - Bali", "Boeing")
pesawatA.info() 

#Contoh 6:
class Kalkulator:     
    @staticmethod
    def add(x, y):
        return x + y      
    @staticmethod     
    def subtract(x, y):
        return x - y      
    @staticmethod     
    def multiply(x, y):
        return x * y      
    @staticmethod
    def divide(x, y):
        if y == 0:             
            raise ValueError('Tidak dapat membagi dengan nol.')
        return x / y 
 
# Memanggil metode statis add() dan subtract() di dalam class Math
print(Kalkulator.add(3, 5))       # Output: 8
print(Kalkulator.subtract(10, 7)) # Output: 3 
 
# Memanggil metode statis multiply() dan divide() di dalam class Math
print(Kalkulator.multiply(4, 6))  # Output: 24 
print(Kalkulator.divide(12, 4))   # Output: 3.0 
 
#Contoh 7: 
class Celcius: 
    @staticmethod
    def to_fahrenheit(celsius):
        return (celsius * 9/5) + 32 
    
    @staticmethod
    def to_kelvin(celsius):
        return celsius + 273.15
    @staticmethod
    def to_reamur(celsius):
        return celsius * 4/5 

mycelcius = 80
myfahrenheit = Celcius.to_fahrenheit(mycelcius)
print(myfahrenheit) 
