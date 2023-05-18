class Employee:
    def detail(self,name,salary):
        self.name = name
        self.salary = salary

    def showData(self):
        print("ชื่อพนักงาน {}".format(self.name))
        print("เงินเดือน {}".format(self.salary))

obj1 = Employee()
obj1.detail("Sorawit",23000)

obj2 = Employee()
obj2.detail("Namcha",30000)

obj1.showData()
obj2.showData()