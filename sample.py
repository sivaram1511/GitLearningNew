class X:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("m1 method of x class")
    @classmethod
    def m2(cls):
        print("m2class method  of paren class")
    @staticmethod
    def m3():
        print("parent class static method")
class Y(X):
    def __init__(self):
        self.c=30
        super().__init__()
y=Y()
y.m3()
y.m2()
y.m1()
print(y.a)
print(y.b)
print(y.c)
        


