class Test:
    x=10
    def __init__(self):
        print(self.x)
        print(Test.x)

        
    def m1(self):
        print(self.x)
        print(Test.x)
    @classmethod
    def m2(cls):
        print(cls.x)
        print(Test.x)
    @staticmethod
    def m3():
        print(Test.x)
t=Test()
t.m1()
t.m2()
t.m3()
print(Test.x)
print(t.x)
        
       
    
        




