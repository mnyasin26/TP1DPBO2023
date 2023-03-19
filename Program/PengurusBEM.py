# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Mahasiswa import Mahasiswa

class PengurusBEM(Mahasiswa):
    # protected attributes
    _kabinet = ""
    _jabatan = ""
    _program = ""

    # Constructor with default value
    def __init__(self, nik="", nama="", alamat="", jenisKelamin="", nim="", semester="", ipk="", prodi="", kabinet="", jabatan="", program=""):
        super().__init__(nik, nama, alamat, jenisKelamin, nim, semester, ipk, prodi)
        self._kabinet = kabinet
        self._jabatan = jabatan
        self._program = program

    # --- Setters ---
    def setKabinet(self, kabinet):
        self._kabinet = kabinet

    def setJabatan(self, jabatan):
        self._jabatan = jabatan

    def setprogram(self, program):
        self._program = program

    # --- Getters ---
    def getKabinet(self):
        return self._kabinet
    
    def getJabatan(self):
        return self._jabatan

    def getprogram(self):
        return self._program
    
    # signature Methods
    def doProgram(self):
        print(self._program + " is being Excexuted by " + self._nama)

    def makeInnovation(self):
        print(self._nama + " is creating Innovation...")

    def doInnovation(self):
        print(self._nama + " is doing Inniovation...")

