# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Manusia import Manusia

class Mahasiswa(Manusia):
    # protected attributes
    _nim = ""
    _semester = ""
    _ipk = ""
    _prodi = ""
    _Laptop = ""

    # Constructor with default value
    def __init__(self, nik="", nama="", alamat="", jenisKelamin="", nim="", semester="", ipk="", prodi=""):
        super().__init__(nik, nama, alamat, jenisKelamin)
        self._nim = nim
        self._semester = semester
        self._ipk = ipk
        self._prodi = prodi

    # --- Setters ---
    def setNim(self, nim):
        self._nim = nim

    def setSemester(self, semester):
        self._semester = semester

    def setIpk(self, ipk):
        self._ipk = ipk

    def setProdi(self, prodi):
        self._prodi = prodi

    def setLaptop(self, Laptop):
        self._Laptop = Laptop

    # --- Getters ---
    def getNim(self):
        return self._nim
    
    def getSemester(self):
        return self._semester

    def getIpk(self):
        return self._ipk
    
    def getProdi(self):
        return self._prodi
    
    def getLaptop(self):
        return self._Laptop
    
    # signature Methods
    def study(self):
        print(self._nama + " is Studying...")

    def attendClass(self):
        print(self._nama + " is Attending a Class...")

    def doAssignemntWork(self):
        print(self._nama + " is doing Assigment Work...")
