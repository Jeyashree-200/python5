class Employee:
    def __init__(self):
        self.ID = int(input("Enter Employee ID: "))
        self.name =input("Enter Employee Name: ")
        self.basic=int(input("Enter basic salary: "))
    def display(self):
        da=0.10*self.basic
        hra=0.20*self.basic
        g=da+hra+self.basic
        print("....employee details....")
        print("employee ID:",self.ID,"\n employee name,self.name,\nDA:",da)
        print("home rent allowance:",hra,"gross salary:",g)
e=Employee()
e.display()
