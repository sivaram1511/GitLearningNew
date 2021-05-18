class Test:
    x=10
    def __init__(self):
        Test.y=20

        
    def m1(self):
        Test.z=30
    @classmethod
    def m2(cls):
        cls.p1=40
        Test.p2=50
    @staticmethod
    def m3():
        Test.q=60
print(Test.__dict__)
Test.f=70
print(Test.__dict__)
        
       
    
        




