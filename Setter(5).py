class Employee: 

    def __init__(self,name,salary):
        #Private attribute
        self.__name = name
        self.__salary = salary

    
    def _showData(self):
        #Private Method
        print("ชื่อพนักงาน {}".format(self.getname()))
        print("เงินเดือน {}".format(self.getsalary()))

    #Setter Method
    def setName(self,newname):
        self.__name = newname

    def setsalary(self,newsalary):
        self.__salary = newsalary

    #Getter Method
    def getname(self):
        return self.__name
    def getsalary(self):
        return self.__salary

obj1 = Employee("Sorawit",23000)
#obj1.setName('Namcha')
#obj1.setsalary(40000)
obj1._showData()



