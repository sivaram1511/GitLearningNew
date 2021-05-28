import csv
with open("emp.csv","w",newline='')as f:
    w=csv.writer(f)
    w.writerow(["Eno","Ename","Esal","Eaddr"])
    n=int(input("Enter number ofemployee:"))
    for i in range(n):
        eno=input("enter employee No:")
        ename=input("Enter Employee Name:")
        esal=input("enter employee salary:")
        eaddr=input("enter employee address:")
        w.writerow([eno,ename,esal,eaddr])
print("csv file successfuly")        





