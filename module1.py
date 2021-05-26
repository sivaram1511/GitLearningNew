f=open("abc.txt",'w')
list=["sunny\n","bunny\n","vinny\n","chunny\n"]
f.writelines(list)
print("List of lines written to the file success")
f.close()
