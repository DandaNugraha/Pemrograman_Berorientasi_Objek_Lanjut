class Mobil:
    def __init__(self, NamaMobil, ModelMobil):  
        self.nama = NamaMobil  
        self.model = ModelMobil
 
    def tampilkanNama(self):  
        print(self.nama)  
  
    def tampilkanModel(self):  
        print(self.model)  

class Id: 
    def __init__(self, CarId):  
        self.CarId = CarId  
  
    def getId(self):  
        return self.CarId  
  
  
class Main(Mobil, Id):
    def __init__(self, nama, model, id): 
        Mobil.__init__(self, nama, model)
        Id.__init__(self, id)  
  
Main1 = Main('Swift', 500, '1')  
Main1.tampilkanNama()
Main1.tampilkanModel()
print(Main1.getId())  