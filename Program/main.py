# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

from Mahasiswa import Mahasiswa
from Laptop import Laptop
from Dosen import Dosen
from PengurusBEM import PengurusBEM
from PengurusDPM import PengurusDPM
from AsistenDosen import AsistenDosen
from Table import Table

# data Dummy
laptopHP = Laptop("HP", "Intel Core i3-3110M", "12GB", "Intel HD 4000", "HDD 512GB")
laptopIdepad3 = Laptop("Lenovo", "Ryzen 5 5500H", "8GB", "RTX 3050", "SSD 512GB")
laptopLegion = Laptop("Lenovo", "Ryzen 5 4500H", "16GB", "GTX 1650", "SSD 512GB")
laptopVictus = Laptop("HP", "Ryzen 5 5500H", "16GB", "RTX 3060", "SSD 512GB")
laptopYoga = Laptop("Lenovo", "Intel Core i5 7232U", "8GB", "Intel UHD 630", "SSD 256GB")
listLaptop = [laptopHP, laptopIdepad3, laptopLegion, laptopVictus, laptopYoga]

rapi = PengurusBEM("19832912245", "Rafi Arsalan Mi'raj", "Sukabumi", "L", "2100345", "4", "3.97", "Ilmu Komputer", "Asmaraloka", "President BEM", "Nongski")
rapi.setLaptop(laptopHP)
alga = PengurusDPM("19832916346", "Alghaniyu Naufal Hamid", "Bekasi", "L", "2100452", "4", "3.85", "Ilmu Komputer", "Antaranata", "Staff DPM", "NgawasRapi", rapi)
alga.setLaptop(laptopIdepad3)

najmi = AsistenDosen("19832914562", "Najma Qalbi Dwiharani", "Cirebon", "P", "2103534", "4", "4.00", "Ilmu Komputer", "13", "Sorting", "Alpro 2")
najmi.setLaptop(laptopLegion)
bulan = AsistenDosen("19832352834", "Muhammad Cahyana Bintang Fajar", "Subang", "L", "2104564", "4", "3.89", "Ilmu Komputer", "13", "Searching", "Alpro 2")
bulan.setLaptop(laptopVictus)

afri = Mahasiswa("19832234526", "Apri Anggara Yudha", "Jateng", "L", "2107854", "4", "3.88", "Ilmu Komputer")
anin = Mahasiswa("19832678456", "Anandita Kusumah Mulyadi", "Bandung", "P", "2105634", "4", "3.92", "Ilmu Komputer")

listAsisten = [najmi, bulan]
mrsRosa = Dosen("1983223489", "Rosa Ariani Sukamto", "Bandung", "P", "123948361", "2", laptopYoga, listAsisten)

#test method
afri.study()
anin.eat()

rapi.doProgram()
alga.supervise()
alga.giveApreciation()

najmi.teaching()
bulan.giveAssignment()

mrsRosa.teaching()
mrsRosa.superviseAssistant()


# Dipslay Data Laptop
headerLaptop = ["Merk","CPU", "RAM", "GPU", "Storage"]
dataLaptop =  Table(headerLaptop)
for n in listLaptop:
    temp = [n.getMerk(), n.getCpu(), n.getRam(), n.getGpu(), n.getStorage()]
    dataLaptop.addRow(temp)
dataLaptop.displayData()