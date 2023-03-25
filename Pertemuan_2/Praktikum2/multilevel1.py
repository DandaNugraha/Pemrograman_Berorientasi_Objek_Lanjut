class Manager:
	def tinjauan_akhir(self):
		print("Peninjauan Akhir")
 
class Peninjau(Manager):
	def tinjauan(self):
		print("Sedang Meninjau...")
 
class Penulis(Peninjau):
	def menulis(self):
		print("Menulis")
 
o = Penulis()
o.tinjauan_akhir()
o.tinjauan()
o.menulis()