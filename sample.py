print("Hello python")
s1=input("Enter main String")
s2=input("Enter sub String")
flag=False
pos=-1
n=len(s1)
while True:
    pos=s1.find(s2,pos+1,n)
    if pos==-1:
        break
    print("found the substring",pos)
    flag=True
if flag==False:
    print("not Found it")
print(s1.count(s2))    





































    
  






  



        


   





    




        
     

   



   







