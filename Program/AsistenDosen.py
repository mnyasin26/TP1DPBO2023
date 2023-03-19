# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Mahasiswa import Mahasiswa

class AsistenDosen(Mahasiswa):
    # protected attributes
    _angaktan = ""
    _bagianMateri = ""
    _matkul = ""

    # Constructor with default value
    def __init__(self, nik="", nama="", alamat="", jenisKelamin="", nim="", semester="", ipk="", prodi="", angaktan="", bagianMateri="", matkul=""):
        super().__init__(nik, nama, alamat, jenisKelamin, nim, semester, ipk, prodi)
        self._angaktan = angaktan
        self._bagianMateri = bagianMateri
        self._matkul = matkul

    # --- Setters ---
    def setAngaktan(self, angaktan):
        self._angaktan = angaktan

    def setBagianMateri(self, bagianMateri):
        self._bagianMateri = bagianMateri

    def setMatkul(self, matkul):
        self._matkul = matkul

    # --- Getters ---
    def getAngaktan(self):
        return self._angaktan
    
    def getBagianMateri(self):
        return self._bagianMateri

    def getMatkul(self):
        return self._matkul
    
    # signature Methods
    def teaching(self):
        print(self._nama + " is Teaching...")

    def giveAssignment(self):
        print(self._nama + " is Giving Assignment...")

    def giveScore(self):
        print(self._nama + " is Giving Score...")
