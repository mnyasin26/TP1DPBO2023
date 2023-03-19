# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

class Laptop():
    # protected attributes
    _merk = ""
    _cpu = ""
    _ram = ""
    _gpu = ""
    _storage = ""

    # Constructor with default value
    def __init__(self, merk="", cpu="", ram="", gpu="", storage=""):
        self._merk = merk
        self._cpu = cpu
        self._ram = ram
        self._gpu = gpu
        self._storage = storage

    # --- Setters ---
    def setMerk(self, merk):
        self._merk = merk

    def setCpu(self, cpu):
        self._cpu = cpu

    def setRam(self, ram):
        self._ram = ram

    def setGpu(self, gpu):
        self._gpu = gpu

    def setStorage(self, storage):
        self._storage = storage

    # --- Getters ---
    def getMerk(self):
        return self._merk
    
    def getCpu(self):
        return self._cpu

    def getRam(self):
        return self._ram
    
    def getGpu(self):
        return self._gpu
    
    def getStorage(self):
        return self._storage
    
    # signature Methods
    def turnOn():
        print("turning On laptop...")

    def turnOn():
        print("turning Off laptop...")

