l=[]
l1=[]
n=int(input("enter the limit of the list"))
for i in range(1,n+1):
     n1=int(input())
     l.append(n1)
print("old list",l)
for i in l:
    if i>100:
        l1.append("over")
    else:
        l1.append(i)
print("new list",l1)
