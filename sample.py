class Book:

   def __init__(self,pages):
        self.pages=pages
   def __add__(self,other):
        total=self.pages+other.pages
        return Book(total)
   def __str__(self):
       return str(self.pages)
b1=Book(100)
b2=Book(200)
b3=Book(200)
bx=b1+b2+b3
print("The total Number of pages",bx)
    

        


