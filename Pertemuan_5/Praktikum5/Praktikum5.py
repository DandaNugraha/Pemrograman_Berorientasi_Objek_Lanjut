#TypeError:
try: 
    def sum(a, b): 
        return a+b
  
    print(sum(2, 'b')) 
  
except TypeError: 
    print("TypeError terjadi karena mencoba untuk menambahkan tipe data yang tidak cocok") 
    
#ZeroDivisionError:
try: 
    print(1/0) 

except ZeroDivisionError: 
    print("ZeroDivisionError terjadi karena mencoba untuk membagi dengan nol") 
    
#FileNotFound:
try: 
    f = open('test.txt') 

except FileNotFoundError: 
    print("FileNotFoundError terjadi karena mencoba untuk membuka file yang tidak ada") 
    
#KeyError:
try: 
    d = {'a': 1, 'b': 2}
    print(d['c']) 

except KeyError: 
    print("KeyError terjadi karena mencoba untuk mengakses kunci yang tidak ada dalam dictionary") 

#IndexError:
try: 
    list = [1, 2, 3]
    print(list[3]) 

except IndexError: 
    print("IndexError terjadi karena mencoba untuk mengakses indeks yang melebihi jumlah item di dalam list") 

#AttributeError:
try: 
    t = (1, 2, 3)
    print(t.append(4)) 

except AttributeError: 
    print("AttributeError terjadi karena mencoba untuk menggunakan atribut yang tidak cocok untuk tipe data") 

#ValueError:
try: 
    n = int("abc") 

except ValueError: 
    print("ValueError terjadi karena mencoba untuk mengkonversi string yang tidak dapat dikonversi ke tipe data yang sesuai") 

#NameError:
try: 
    print(x) 

except NameError: 
    print("NameError terjadi karena mencoba untuk menggunakan variabel yang tidak didefinisikan") 

#KeyboardInterrupt:
try: 
    while True: 
        pass

except KeyboardInterrupt: 
    print("KeyboardInterrupt terjadi karena menekan tombol CTRL + C pada keyboard") 

#MemoryError:
try: 
    x = []
    while True: 
        x.append(1) 

except MemoryError: 
    print("MemoryError terjadi karena memori yang tersedia sudah habis")