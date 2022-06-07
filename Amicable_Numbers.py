m=int(input())
n=int(input())
Sum=0
b=0
for i in range(1,m):
    if(m%i==0):
        Sum=Sum+i
for j in range(1,n):
    if(n%j==0):
        b=b+j
if(m==b and n==Sum):
    print("Amicable")
else:
    print("Not Amicable")