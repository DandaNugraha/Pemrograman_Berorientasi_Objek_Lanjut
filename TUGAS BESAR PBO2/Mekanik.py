import requests
import json
class Mekanik:
    def __init__(self):
        self.__id=None
        self.__kode_mekanik = None
        self.__nama = None
        self.__telepon = None
        self.__alamat = None
        self.__spesialis = None
        self.__status = None
        self.__url = "http://f0832646.xsph.ru/datajasa/mekanik_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_mekanik(self):
        return self.__kode_mekanik
        
    @kode_mekanik.setter
    def kode_mekanik(self, value):
        self.__kode_mekanik = value
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
    def spesialis(self):
        return self.__spesialis
        
    @spesialis.setter
    def spesialis(self, value):
        self.__spesialis = value
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
    def get_by_kode_mekanik(self, kode_mekanik):
        url = self.__url+"?kode_mekanik="+kode_mekanik
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_mekanik']
            self.__kode_mekanik = item['kode_mekanik']
            self.__nama = item['nama']
            self.__telepon = item['telepon']
            self.__alamat = item['alamat']
            self.__spesialis = item['spesialis']
            self.__status = item['status']
        return data
    def simpan(self):
        payload = {
            "kode_mekanik":self.__kode_mekanik,
            "nama":self.__nama,
            "telepon":self.__telepon,
            "alamat":self.__alamat,
            "spesialis":self.__spesialis,
            "status":self.__status
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_mekanik(self, kode_mekanik):
        url = self.__url+"?kode_mekanik="+kode_mekanik
        payload = {
            "kode_mekanik":self.__kode_mekanik,
            "nama":self.__nama,
            "telepon":self.__telepon,
            "alamat":self.__alamat,
            "spesialis":self.__spesialis,
            "status":self.__status
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_mekanik(self,kode_mekanik):
        url = self.__url+"?kode_mekanik="+kode_mekanik
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text