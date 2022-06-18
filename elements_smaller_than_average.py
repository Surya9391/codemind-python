n=int(input())
a=list(map(int,input().strip().split()))
c=0
avg=sum(a)//len(a)
for i in range(0,len(a)):
    if(a[i]<=avg):
        c+=1
print(c)        