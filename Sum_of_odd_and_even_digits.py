n=int(input())
a=list(map(int,input().split()))
s=0
k=0
for i in range(n):
    if(i%2==0):
        s=s+(a[i])
for j in range(n):
    if(j%2!=0):
        k=k+(a[j])
if(s-k==0):
    print("YES")
else:
    print("NO")