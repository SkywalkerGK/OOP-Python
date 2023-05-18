class Employee:
    def detail(self):
        self.name = "Sorawit"
        self.salary = 23000
        print("ชื่อพนักงาน {}".format(self.name))
        print("เงินเดือน {}".format(self.salary))
        
emp1 = Employee()
emp1.detail()