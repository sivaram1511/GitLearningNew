class P:
    def __init__(self):
        print("parent class Constructor")
    
    def marry(self):
        print("Applamma ")
class C(P):
    def __init__(self):
        super().__init__()
        print("child class Constructor")
    def marry(self):
        super().marry()
        print("Katrina Kaif and appalamma both of them intereste")
c=C()
c.marry()

