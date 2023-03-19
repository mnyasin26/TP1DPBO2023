# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

class Manusia:
    # protected attributes
    _noKTP = ""
    _nama = ""
    _alamat = ""
    _jenisKelamin=""

    # Constructor with default value
    def __init__(self, noKTP="", nama="", alamat="", jenisKelamin=""):
        self._noKTP = noKTP
        self._nama = nama
        self._alamat = alamat
        self._jenisKelamin = jenisKelamin

    # --- Setters ---
    def setNoKTP(self, noKTP):
        self._noKTP = noKTP

    def setNama(self, nama):
        self._nama = nama

    def setAlamat(self, alamat):
        self._alamat = alamat
        
    def setJenisKelamin(self, jenisKelamin):
        self._jenisKelamin = jenisKelamin

    # --- Getters ---
    def getnoKTP(self):
        return self._noKTP

    def getNama(self):
        return self._nama

    def getAlamat(self):
        return self._alamat
    
    def getJenisKelamin(self):
        return self._jenisKelamin

    # signature Methods
    def eat(self):
        print(self._nama + " is Eating...")

    def sleep(self):
        print(self._nama + " is Sleep...")