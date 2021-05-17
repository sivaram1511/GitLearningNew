from functools import *
l=[46,42,87,96,58,25,14]
def doublelt(x):
    return x*2
l1=list(map(doublelt,l))
print(l1)
l2=list(map(lambda x:x*2,l))
print(l2)
l3=reduce(lambda x,y:x+y,l)
print(l3)
l4=reduce(lambda x,y:x*y,l)
print(l4)

        




