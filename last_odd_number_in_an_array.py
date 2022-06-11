n=int(input())
arr=list(map(int,input().strip().split()))[:n]
for i in range(0,len(arr)):
    if(arr[i]%2!=0):
        c=arr[i]
print(c)        