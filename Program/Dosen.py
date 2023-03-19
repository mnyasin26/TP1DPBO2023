# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Manusia import Manusia
from AsistenDosen import AsistenDosen


class Dosen(Manusia):
    # protected attributes
    _nip = ""
    _jmlhSpidol = ""
    _Laptop = ""
    _AsistenDosen : list[AsistenDosen]

    # Constructor with default value
    def __init__(self, nik="", nama="", alamat="", jenisKelamin="", nip="", jmlhSpidol="", Laptop="", AsistenDosen=[]):
        super().__init__(nik, nama, alamat, jenisKelamin)
        self._nip = nip
        self._jmlhSpidol = jmlhSpidol
        self._Laptop = Laptop
        self._AsistenDosen = AsistenDosen

    # --- Setters ---
    def setNip(self, nip):
        self._nip = nip

    def setJmlhSpidol(self, jmlhSpidol):
        self._jmlhSpidol = jmlhSpidol

    def setLaptop(self, Laptop):
        self._Laptop = Laptop

    def setAsistenDosen(self, AsistenDosen):
        self._AsistenDosen = AsistenDosen

    # --- Getters ---
    def getNip(self):
        return self._nip

    def getJmlhSpidol(self):
        return self._jmlhSpidol

    def getLaptop(self):
        return self._Laptop
    
    def getAsistenDosen(self):
        return self._AsistenDosen
    
    # signature Methods
    def teaching(self):
        print(self._nama + " is Teaching...")

    def giveAssignment(self):
        print(self._nama + " is Giving Assignment...")

    def giveScore(self):
        print(self._nama + " is Giving Score...")

    def superviseAssistant(self):
        for i in self._AsistenDosen:
            print(i.getNama() + " is being Supervised by " + self._nama)
