class P:
    def property(self):
        print("Gold+Land+Cash+Power")
    def marry(self):
        print("Applamma")
class C(P):
    def marry(self):
        super().marry()
        print("Katrina Kaif")
c=C()
c.property()
c.marry()

