n=int(input())
sum=0
Mul=1
while(n>0):
    d=n%10
    sum=sum+d
    Mul=Mul*d
    n=n//10
if sum==Mul:
    print('Spy Number')
else:
    print('Not Spy Number')