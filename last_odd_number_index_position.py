n=int(input())
c=0
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    if(arr[i]%2!=0):
        c=i
print(c)        
