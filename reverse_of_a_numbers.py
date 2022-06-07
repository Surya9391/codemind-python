n=int(input())
temp=n
rem=0
while n>0:
    d=n%10
    rem=rem*10+d
    n=n//10
print(rem)    