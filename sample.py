class P:
    a=20
    def __init__(self):
        self.b=30
class C(P):
    def __init__(self):
        self.c=40
    def m1(self):
        print(super().a)
        #print(super().b)
        print(self.c)
c=C()
c.m1()
    

        


