s=input("Enter some String")

l=[]
for x in s:
    if x not in l:
        l.append(x)
output=''.join(l)
print(output)
    
        

    

