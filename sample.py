class P:
    def __init__(self):
        print("parent class Constructor")
    
    def marry(self):
        print("Applamma")
class C(P):
    def __init__(self):
        print("child class Constructor")
    def marry(self):
        super().marry()
        print("Katrina Kaif")
c=C()
c.marry()

