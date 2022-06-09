a=int(input())
b=a*a
Sum=0
while(b>0):
    d=b%10
    Sum=Sum+d
    b=b//10
if(Sum==a):
    print('Neon Number')
else:
    print('Not Neon Number')