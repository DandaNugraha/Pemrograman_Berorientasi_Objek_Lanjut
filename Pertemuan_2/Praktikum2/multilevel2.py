class Keluarga:
	def show(self):
		print("Keluargaku....") 
 
class OrangTua(Keluarga):
	nama_ayah = ""
	nama_ibu = ""

	def show1(self):
	    print(self.nama_ayah)
	    
 
class Anak(OrangTua):
	nama_anak = ""

	def show2(self):
		print("Nama Ayah :",self.nama_ayah)
		print("Nama Ibu :",self.nama_ibu)
		print("Nama Anak :",self.nama_anak)
 
o = Anak()
o.nama_ayah = "Fahgi"
o.nama_ibu = "Rima"
o.nama_anak = "Gihfa"
o.show()
o.show2()