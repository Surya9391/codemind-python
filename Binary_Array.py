n=int(input())
a=list(map(int,input().strip().split()))[:n]
c=0
for i in range(0,len(a)):
    if((a[i]==0 or a[i]==1)):
        c+=1
if c==n:
    print("True")
else:
    print("False")