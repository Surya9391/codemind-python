n=int(input())
b=int(n**2)
temp=n
Sum=0
while(n!=0):
    d=n%10
    Sum=Sum*10+d
    n=n//10
c=int(Sum**2)
temp=c
rev=0
while(c!=0):
    e=c%10
    rev=rev*10+e
    c=c//10
if(rev==b):
    print("True")
else:
    print("False")