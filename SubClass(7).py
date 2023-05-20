class Employee: 
    #class variable
    minsalary = 12000
    __maxsalary = 50000
    companyname = "บริษัท ABC"


    def __init__(self,name,salary):
        #instance variable
        self.__name = name
        self._salary = salary

    
    def _showData(self):
        print("ชื่อพนักงาน {}".format(self.__name))
        print("เงินเดือน {}".format(self._salary))

class Accounting(Employee):
    def __init__(self):
        pass


class Programmer(Employee):
    def __init__(self):
        pass
class Sale(Employee):
    def __init__(self):
        pass

account = Accounting()
programmer = Programmer()
sale = Sale()
print(account.companyname)
print(programmer._Employee__maxsalary) #Private



#obj1 = Employee("Sorawit",23000)
#print(obj1._salary)
#print(Employee.minsalary) #เข้าถึงได้โดยไม่ต้องสร้าง obj

