class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Eployee Number:",self.eno)
        print("Employee Name:",self.ename)
        print("Employee esal: ",self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+1000
        emp.display()
e=Employee(100,'hitesh',60000)
Test.modify(e)



