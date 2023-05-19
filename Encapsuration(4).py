class Employee: 

    def __init__(self,name,salary):
        print("Defalut Constructor")
        #Public attribute
        self._name = name
        #Private attribute
        self.__salary = salary

        self.__showData()

    
    def __showData(self):
        #Pubric Method
        print("ชื่อพนักงาน {}".format(self._name))
        #Private Method
        print("เงินเดือน {}".format(self.__salary))


obj1 = Employee("Sorawit",23000)
obj1._name = "Namcha"
obj1.__salary = 50000
#obj1.__showData()  Private ภายนอกเอาไปสร้าง object เรียกใช้งานไม่ได้


