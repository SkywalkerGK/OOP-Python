class Employee: 

    def __init__(self):
        print("Defalut Constructor")

    def detail(self,name,salary):
        self.name = name
        self.salary = salary

    def showData(self):
        print("ชื่อพนักงาน {}".format(self.name))
        print("เงินเดือน {}".format(self.salary))

obj1 = Employee()
obj2 = Employee()

