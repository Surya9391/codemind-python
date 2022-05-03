a=int(input())
Sum=0
sqt=a*a
while(sqt!=0):
    d=sqt%10
    Sum=Sum+d
    sqt=sqt//10
    
if(Sum==a):
    print('Neon Number')
else:
    print('Not Neon Number')