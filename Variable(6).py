class Employee: 
    #class variable
    _minsalary = 12000
    _maxsalary = 50000
    __companyname = "บริษัท ABC"


    def __init__(self,name,salary):
        #instance variable
        self.__name = name
        self._salary = salary

    
    def _showData(self):
        print("ชื่อพนักงาน {}".format(self.__name))
        print("เงินเดือน {}".format(self._salary))

#obj1 = Employee("Sorawit",23000)
#print(obj1._salary)
print(Employee._minsalary) #เข้าถึงได้โดยไม่ต้องสร้าง obj



