#Kode Bangun Datar Lingkaran

class LingkaranMeta(type): 
    def __init__(cls, name, bases, attrs): 
        super().__init__(name, bases, attrs) 
        # Tambahkan method untuk menghitung luas dan keliling lingkaran 
    def luas(cls, jari): 
        return 3.14 * (jari**2) 
        cls.luas = classmethod(luas) 
    def keliling(cls, jari): 
        return 2 * 3.14 * jari 
        cls.keliling = classmethod(keliling) 

class Lingkaran(metaclass=LingkaranMeta): 
    pass 

l = Lingkaran() 
# Menghitung luas lingkaran dengan jari-jari=7 
luas_lingkaran = Lingkaran.luas(7) 
print("Luas lingkaran:", luas_lingkaran) 
# Menghitung keliling lingkaran dengan jari-jari=7 
keliling_lingkaran = Lingkaran.keliling(7) 
print("Keliling lingkaran:", keliling_lingkaran)

#Kode Bangun Datar Jajar Genjang

class JajarGenjangMeta(type): 
    def __init__(cls, name, bases, attrs): 
        super().__init__(name, bases, attrs) 
        # Tambahkan method untuk menghitung luas dan keliling jajar genjang
        def luas(cls, alas, tinggi): 
            return alas * tinggi 
        cls.luas = classmethod(luas) 
        def keliling(cls, sisi1, sisi2, sisi3, sisi4): 
            return sisi1 + sisi2 + sisi3 + sisi4 
        cls.keliling = classmethod(keliling) 

class JajarGenjang(metaclass=JajarGenjangMeta): 
    pass 

j = JajarGenjang() 
# Menghitung luas jajar genjang dengan alas=4 dan tinggi=5 
luas_jajar_genjang = JajarGenjang.luas(4, 5) 
print("Luas jajar genjang:", luas_jajar_genjang) 
# Menghitung keliling jajar genjang dengan sisi1=3, sisi2=4, sisi3=5, dan sisi4=6
keliling_jajar_genjang = JajarGenjang.keliling(3, 4, 5, 6) 
print("Keliling jajar genjang:", keliling_jajar_genjang)

#Kode Bangun Datar Trapesium

class TrapesiumMeta(type): 
    def __init__(cls, name, bases, attrs): 
        super().__init__(name, bases, attrs) 
        # Tambahkan method untuk menghitung luas dan keliling trapesium 
        def luas(cls, alas, tinggi): 
            return (alas + tinggi) / 2 * tinggi 
        cls.luas = classmethod(luas) 
        def keliling(cls, sisi1, sisi2, sisi3, sisi4): 
            return sisi1 + sisi2 + sisi3 + sisi4 
        cls.keliling = classmethod(keliling) 

class Trapesium(metaclass=TrapesiumMeta): 
    pass 

t = Trapesium() 
# Menghitung luas trapesium dengan alas=4 dan tinggi=5 
luas_trapesium = Trapesium.luas(4, 5) 
print("Luas trapesium:", luas_trapesium) 
# Menghitung keliling trapesium dengan sisi1=3, sisi2=4, sisi3=5, dan sisi4=6 
keliling_trapesium = Trapesium.keliling(3, 4, 5, 6) 
print("Keliling trapesium:", keliling_trapesium)