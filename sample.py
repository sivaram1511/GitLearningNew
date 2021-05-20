class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks

n=int(input("enter number of students"))
for i in range(n):
    s=Student()
    name=input("name of the student")
    s.setName(name)
    marks=int(input("enter marks"))
    s.setMarks(marks)
print("name of student",s.getName())
print("marks are",s.getMarks())
    
       
    
        




