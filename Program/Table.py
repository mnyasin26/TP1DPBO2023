# Saya Muhamad Nur Yasin Amadudin[2100137] mengerjakan
# TP 1 dalam
# mata kuliah Desain Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan
# kecurangan seperti yang telah dispesifikasikan. Aamiin.

class Table:
    __header : list = [] # buat header table
    __data : list = [] # buat record datanya
    __columnCount = 0
    __colLength = []  # <-- used for table forming

    # contructor definition
    def __init__(self, header):
        self.__columnCount = len(header)
        self.__header = header
        self.__header.insert(0, "No")
        self.__data: list = [] 
        self.__colLength = []  # <-- used for table forming


    def addRow(self, rowData : list):
        if(len(rowData) == self.__columnCount):
            self.__data.append(rowData)
        else:
            print("rowData not matching header countRow")

    # print only: ----------
    def __printBorder(self, len):
        for i in range(len):
            print("-", end="")

    # printing border like: +--------+-------+-----+
    def __printFullBorder(self):
        for n in self.__colLength:
            print("+", end="")
            self.__printBorder(n + 2)
        print("+")

    # calculate longest element on a column
    def __calColLen(self):
        for n in self.__header:
            self.__colLength.append(len(n))

        number = 1
        for n in self.__data:
            n.insert(0, str(number))
            index = 0
            for m in n:
                # checking the longest length of every element corresponds to its column
                if (len(m) > self.__colLength[index]):
                    self.__colLength[index] = len(m)
                index = index + 1
            number = number + 1

    # print spacing
    def __printSpace(self, len):
        for i in range(len):
            print(" ", end="")

    # display attributes (in single row of table)
    def __printAttributes(self, data):
        index = 0
        for n in data:
            print("|", end="")
            print(" " + n, end="")
            self.__printSpace(self.__colLength[index] - len(n) + 1)
            index = index + 1
        print("|")

    # diplay in table format
    def displayData(self):
        self.__calColLen()

        self.__printFullBorder()
        self.__printAttributes(self.__header)
        if len(self.__data) == 0:
            self.__printFullBorder()

        state = 0
        for n in self.__data:
            temp = []
            for m in n:
                temp.append(m)
            self.__printFullBorder()
            self.__printAttributes(temp)

        self.__printFullBorder()
