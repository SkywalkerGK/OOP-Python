class Employee: 

    def __init__(self,name,salary):
        print("Defalut Constructor")
        self.name = name
        self.salary = salary

    def showData(self):
        print("ชื่อพนักงาน {}".format(self.name))
        print("เงินเดือน {}".format(self.salary))


obj1 = Employee("Sorawit",23000)
obj2 = Employee("Namcha",50000)

print(isinstance(obj1,Employee)) #เช็คว่าอยู่ใน Class นี้มั้ย
print(dir(obj1)) #แสดง Attribute Method
print(obj1.__class__) #แสดง Class