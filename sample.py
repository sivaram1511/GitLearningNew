class X:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("m1 method of x class")
class Y:
    c=30
    def __init__(self):
        self.d=40
    def m2(self):
        print("m2 method of Y class")
    def m3(self):
        x=X()
        x.m1()
        print(x.a,x.b)
        print(self.c,self.d)
        self.m2()
y=Y()
y.m3()
        


