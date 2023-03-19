# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Mahasiswa import Mahasiswa
from PengurusBEM import PengurusBEM

class PengurusDPM(Mahasiswa):
    # protected attributes
    _kabinet = ""
    _jabatan = ""
    _program = ""
    _PengurusBEM : PengurusBEM = ""

    # Constructor with default value
    def __init__(self, nik="", nama="", alamat="", jenisKelamin="", nim="", semester="", ipk="", prodi="", kabinet="", jabatan="", program="", PengurusBEM=""):
        super().__init__(nik, nama, alamat, jenisKelamin, nim, semester, ipk, prodi)
        self._kabinet = kabinet
        self._jabatan = jabatan
        self._program = program
        self._PengurusBEM = PengurusBEM

    # --- Setters ---
    def setKabinet(self, kabinet):
        self._kabinet = kabinet

    def setJabatan(self, jabatan):
        self._jabatan = jabatan

    def setprogram(self, program):
        self._program = program

    def setPengurusBEM(self, PengurusBEM):
        self._PengurusBEM = PengurusBEM

    # --- Getters ---
    def getKabinet(self):
        return self._kabinet
    
    def getJabatan(self):
        return self._jabatan

    def getprogram(self):
        return self._program
    
    def getPengurusBEM(self):
        return self._PengurusBEM
    
    # signature Methods
    def supervise(self):
        print(self._PengurusBEM.getNama() + " is being Supervised by " + self._nama)

    def giveApreciation(self):
        print(self._PengurusBEM.getNama() + ", you are amazing, well done, I appreciate your work...")

