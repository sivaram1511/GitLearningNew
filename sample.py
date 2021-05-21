class P:
    a=20
    def __init__(self):
        print("parent class constuctor")
        self.b=30
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("cls method")
    @staticmethod
    def m3():
        print("static method")
class C(P):
    
    @staticmethod
    def m2():
        
        super(C,C).m3()
C.m2()
    

        


