class Parent_class(object): 
        
    def __init__(self, nama, id): 
        self.nama = nama 
        self.id = id
   
    def Detail_Pegawai(self): 
        return self.id , self.nama
   
    def Cek_Pegawai(self): 
        if self.id > 500000:
           return "Pegawai Valid"
        else:
           return "Pegawai tidak valid "
   
   
class Child_class(Parent_class): 
    
    def End(self):
        print( "AKHIRI PROGRAM" ) 
      
Pegawai1 = Parent_class( "Pegawai1" , 600445)
print( Pegawai1.Detail_Pegawai() , Pegawai1.Cek_Pegawai() ) 
Pegawai2 = Child_class( "Pegawai2" , 198754)
print( Pegawai2.Detail_Pegawai() , Pegawai2.Cek_Pegawai() ) 
Pegawai2.End()