class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The Sum of Three Numbers:",a+b+c)
        elif a!=None and b!=None:
            print("The Sum of 2number s",a+b)
        else:
            print("please provide 2 or 3 arguments")
t=Test()
t.sum(10,20)
t.sum(10,20,30)
t.sum(10)
        


