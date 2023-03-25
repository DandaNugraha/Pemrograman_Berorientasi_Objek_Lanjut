class Brand:                     
    nama_brand_1= "Shopee"
    nama_brand_2 = "Tokopedia"
    nama_brand_3 = "OLX"
    
class Produk(Brand):            
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"

class Popularitas(Brand):        
    popularitas_prod_1 = 100
    popularitas_prod_2 = 70
    popularitas_prod_3 = 60

class Nilai(Brand):
    nilai_prod_1 = "Nilai yang Luar Biasa"
    nilai_prod_2 = "Nilai yang Lebih Baik"
    nilai_prod_3 = "Nilai yang Bagus"
    
obj_1 = Produk()
obj_2 = Popularitas()
obj_3 = Nilai()
print(obj_1.nama_brand_1+" adalah "+obj_1.prod_1+" dengan popularitas "+str(obj_2.popularitas_prod_1)+" dan memiliki "+obj_3.nilai_prod_1)
print(obj_1.nama_brand_2+" adalah "+obj_1.prod_2+" dengan popularitas "+str(obj_2.popularitas_prod_2)+" dan memiliki "+obj_3.nilai_prod_2)
print(obj_1.nama_brand_3+" adalah "+obj_1.prod_3+" dengan popularitas "+str(obj_2.popularitas_prod_3)+" dan memiliki "+obj_3.nilai_prod_3)