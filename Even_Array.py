n=int(input())
b=list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,n):
    if(b[i]%2==0):
        c+=1
if(c==n):
    print("True")
else:
    print("False")