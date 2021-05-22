class Test:
    def __init__(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("Sum os a b c",a+b+c)
        elif a!=None and b!=None:
            print("Sum of a,b",a+b)
        else:
            print("at least two argumnets")

       
        

t1=Test()
t2=Test(10,20)
t3=Test(10,20,30)
        


