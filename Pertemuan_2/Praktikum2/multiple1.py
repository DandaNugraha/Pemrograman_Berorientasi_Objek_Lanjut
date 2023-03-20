class Brands:
    nama_brand_1 = "Amazon"
    nama_brand_2 = "Ebay"
    nama_brand_3 = "OLX"
    
class Products:
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"

class Popularitas(Brands,Products):
    popularitas_prod_1 = 100
    popularitas_prod_2 = 70
    popularitas_prod_3 = 60
    
obj_1 = Popularitas()
print(obj_1.nama_brand_1+" adalah "+obj_1.prod_1)
print(obj_1.nama_brand_2+" adalah "+obj_1.prod_2)
print(obj_1.nama_brand_3+" adalah "+obj_1.prod_3)