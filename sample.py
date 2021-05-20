class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getinfo(self):
        print("Car name:{},Model:{} and color:{}".format(self.name,self.model,self.color))
        
        

class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car
    def empinfo(self):
        print("Name of the Employee:",self.ename)
        print("Employee Number:",self.eno)
        print("Employee car info ")
        self.car.getinfo()
        
    
c=Car("Innova","2.5v","yellow")
e=Employee("sivaram",101,c)
e.empinfo()


