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
    def __init__(self):
        self.c=40
    def m1(self):
        print(super().a)
        #print(super().b)
        print(self.c)
    @classmethod
    def m1(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)
        super().m2()
        super().m3()
c=C()
c.m1()
    

        


