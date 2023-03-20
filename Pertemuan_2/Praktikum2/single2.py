class Parent_class(object): 
       
    def __init__(self, Nilai1,Nilai2): 
        self.Nilai1 = Nilai1 
        self.Nilai2 = Nilai2
   
    def Pertambahan(self) : 
        print(" Pertambahan Nilai1 : " , self.Nilai1)
        print(" Pertambahan Nilai2 : " , self.Nilai2)
        return self.Nilai1 + self.Nilai2
        
    def Perkalian(self) :
        print(" Perkalian Nilai1 : " , self.Nilai1)
        print(" Perkalian Nilai2 : " , self.Nilai2)
        return self.Nilai1 * self.Nilai2
        
    def Pengurangan(self) :
        print(" Pengurangan Nilai1 : " , self.Nilai1)
        print(" Pengurangan Nilai2 : " , self.Nilai2)
        return self.Nilai1 - self.Nilai2
      
class Child_class(Parent_class): 
    
    pass
      
Object1 = Child_class(10,15)
print(" Pertambahan:" , Object1.Pertambahan() ) 
print( " " )
Object2 = Child_class(20,30)
print(" Perkalian:" , Object2.Perkalian() ) 
print( " " )
Object3 = Child_class(50,30)
print(" Pengurangan:" , Object3.Pengurangan() ) 