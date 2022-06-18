n=int(input())
a=list(map(int,input().strip().split()))[:n]
even=[]
odd=[]
for i in range(0,len(a)):
    if(a[i]%2==0):
        even.append(a[i])
for j in range(0,len(a)):
    if(a[j]%2!=0):
        odd.append(a[j])
c=odd+even
print(*c)