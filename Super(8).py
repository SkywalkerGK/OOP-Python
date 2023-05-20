class Employee: 
    #class variable
    minsalary = 12000
    maxsalary = 50000
    companyname = "บริษัท ABC"

    def __init__(self,name,salary,department):
        #instance variable
        self.__name = name
        self._salary = salary
        self.department = department

    def _showData(self):
        print("ชื่อพนักงาน {}".format(self.__name))
        print("เงินเดือน {}".format(self._salary))
        print("ตำแหน่งงาน {}".format(self.department))

class Accounting(Employee):
    __departmentName = "แผนกบัญชี"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()

class Programmer(Employee):
    __departmentName = "แผนกเขียนโปรแกรม"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()


class Sale(Employee):
    __departmentName = "ฝ่ายขาย"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()


account = Accounting("Namchom",15000)
programmer = Programmer("Bass",23000)
sale = Sale("Namcha",50000)

#account._showData()
#programmer._showData()
#sale._showData()

