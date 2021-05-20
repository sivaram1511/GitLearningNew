class Engine:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print("Engine class members")
class Car:
    def __init__(self):
        self.engine=self.Engine()
    def m2(self):
        print("Car using Engine class Functionalities")
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()
c=Car()
c.m2()


