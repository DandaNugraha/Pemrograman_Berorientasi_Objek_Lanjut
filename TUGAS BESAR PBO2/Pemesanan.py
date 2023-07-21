import requests
import json
class Pemesanan:
    def __init__(self):
        self.__id=None
        self.__kode_pemesanan = None
        self.__id_user = None
        self.__tanggal = None
        self.__nama = None
        self.__telepon = None
        self.__alamat = None
        self.__jenis_jasa = None
        self.__keluhan = None
        self.__total_biaya = None
        self.__mekanik = None
        self.__keterangan = None
        self.__status = None
        self.__url = "http://f0832646.xsph.ru/datajasa/pemesanan_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_pemesanan(self):
        return self.__kode_pemesanan
        
    @kode_pemesanan.setter
    def kode_pemesanan(self, value):
        self.__kode_pemesanan = value
    @property
    def id_user(self):
        return self.__id_user
        
    @id_user.setter
    def id_user(self, value):
        self.__id_user = value
    @property
    def tanggal(self):
        return self.__tanggal
        
    @tanggal.setter
    def tanggal(self, value):
        self.__tanggal = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def telepon(self):
        return self.__telepon
        
    @telepon.setter
    def telepon(self, value):
        self.__telepon = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def jenis_jasa(self):
        return self.__jenis_jasa
        
    @jenis_jasa.setter
    def jenis_jasa(self, value):
        self.__jenis_jasa = value
    @property
    def keluhan(self):
        return self.__keluhan
        
    @keluhan.setter
    def keluhan(self, value):
        self.__keluhan = value
    @property
    def total_biaya(self):
        return self.__total_biaya
        
    @total_biaya.setter
    def total_biaya(self, value):
        self.__total_biaya = value
    @property
    def mekanik(self):
        return self.__mekanik
        
    @mekanik.setter
    def mekanik(self, value):
        self.__mekanik = value
    @property
    def keterangan(self):
        return self.__keterangan
        
    @keterangan.setter
    def keterangan(self, value):
        self.__keterangan = value
    @property
    def status(self):
        return self.__status
        
    @status.setter
    def status(self, value):
        self.__status = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    
    def get_by_kode_pemesanan(self, kode_pemesanan):
        url = self.__url+"?kode_pemesanan="+kode_pemesanan
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_pemesanan']
            self.__kode_pemesanan = item['kode_pemesanan']
            self.__id_user = item['id_user']
            self.__tanggal = item['tanggal']
            self.__nama = item['nama']
            self.__telepon = item['telepon']
            self.__alamat = item['alamat']
            self.__jenis_jasa = item['jenis_jasa']
            self.__keluhan = item['keluhan']
            self.__total_biaya = item['total_biaya']
            self.__mekanik = item['mekanik']
            self.__keterangan = item['keterangan']
            self.__status = item['status']
        return data

    def get_by_id_user(self, id_user):
        url = self.__url +"?id_user="+str(id_user)
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_pemesanan']
            self.__kode_pemesanan = item['kode_pemesanan']
            self.__id_user = item['id_user']
            self.__tanggal = item['tanggal']
            self.__nama = item['nama']
            self.__telepon = item['telepon']
            self.__alamat = item['alamat']
            self.__jenis_jasa = item['jenis_jasa']
            self.__keluhan = item['keluhan']
            self.__total_biaya = item['total_biaya']
            self.__mekanik = item['mekanik']
            self.__keterangan = item['keterangan']
            self.__status = item['status']
        return data

    def simpan(self):
        payload = {
            "kode_pemesanan":self.__kode_pemesanan,
            "id_user":self.__id_user,
            "tanggal":self.__tanggal,
            "nama":self.__nama,
            "telepon":self.__telepon,
            "alamat":self.__alamat,
            "jenis_jasa":self.__jenis_jasa,
            "keluhan":self.__keluhan,
            "total_biaya":self.__total_biaya,
            "mekanik":self.__mekanik,
            "keterangan":self.__keterangan,
            "status":self.__status
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    
    def update_by_kode_pemesanan(self, kode_pemesanan):
        url = self.__url+"?kode_pemesanan="+kode_pemesanan
        payload = {
            "kode_pemesanan":self.__kode_pemesanan,
            "id_user":self.__id_user,
            "tanggal":self.__tanggal,
            "nama":self.__nama,
            "telepon":self.__telepon,
            "alamat":self.__alamat,
            "jenis_jasa":self.__jenis_jasa,
            "keluhan":self.__keluhan,
            "total_biaya":self.__total_biaya,
            "mekanik":self.__mekanik,
            "keterangan":self.__keterangan,
            "status":self.__status
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    
    def delete_by_kode_pemesanan(self,kode_pemesanan):
        url = self.__url+"?kode_pemesanan="+kode_pemesanan
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text

    def get_latest_kode_pemesanan(self):
        url = self.__url + "?max_kode_pemesanan=true"
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, headers=headers)

        # Convert the response to JSON format
        data = json.loads(response.text)

        # Check if the response is a list (API returned a list instead of a dictionary)
        if isinstance(data, list):
            # Extract the 'kode_pemesanan' values from the dictionaries in the list
            kode_pemesanans = [int(item.get('kode_pemesanan', 0)) for item in data]

            # Find the maximum kode_pemesanan value
            max_kode_pemesanan = max(kode_pemesanans)

            return max_kode_pemesanan
        else:
            # If the response is a dictionary, get the maximum kode_pemesanan from the dictionary
            max_kode_pemesanan = data.get('max_kode_pemesanan')

            # Check if max_kode_pemesanan is not None and convert it to an integer
            if max_kode_pemesanan is not None:
                return int(max_kode_pemesanan)
            else:
                # Return a default value (e.g., 0) if max_kode_pemesanan is None
                return 0