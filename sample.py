n=int(input("Enter the number of students"))
d={}
for i in range(n):
    name=input("name of the student")
    marks=int(input("Enter marks"))
    d[name]=marks
while True:
    name=input("Enter Student name to get the marks")
    marks=d.get(name,-1)
    if marks==-1:
        print("Stdent not found")
    else:
        print("The marks of", name,"are",marks)
    option=input("do u want find another student marks[yes|no]")
    if option =="no":
        break
print("Thanks for using our applications")    
