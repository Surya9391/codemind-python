def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
                break
        else:
            return True
n=int(input())
l=[]
for i in range(2,n):
    for j in range(2,n):
        if i*j==n:
            l.append(i)
            l.append(j)
            break
if len(l)==0:
    print("-1")
else:
    print(*set(l))
            