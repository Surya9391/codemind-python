a=int(input())
Sum=0
pro=1
while(a>0):
    d=a%10
    Sum=Sum+d
    pro=pro*d
    a=a//10
if(Sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")