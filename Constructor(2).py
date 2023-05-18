class Employee: 

    def __init__(self,name,salary):
        print("Defalut Constructor")
        self.name = name
        self.salary = salary

    def showData(self):
        print("ชื่อพนักงาน {}".format(self.name))
        print("เงินเดือน {}".format(self.salary))

    def __del__(self):
        print("Destructor")

obj1 = Employee("Sorawit",23000)
obj2 = Employee("Namcha",50000)
obj2.salary = 70000

obj1.showData()
obj2.showData()