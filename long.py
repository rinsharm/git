n=input("enter a string")
l=n.split(" ")
b=0
for i in l:
    c=len(i)
    if(b<c):
        b=c
        s=i
print("the longest word is",s,"and its length is",c)
