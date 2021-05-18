class Student:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self):
        self.d=50
s=Student()
s.m1()
s.e=89
print(s.__dict__)
        
    
        




