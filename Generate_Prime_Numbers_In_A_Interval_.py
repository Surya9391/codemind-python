m=int(input())
n=int(input())
for i in range(m+1,n):
    if(i>0):
        for j in range(2,(i//2)+1):
            if(i%j==0):
                break
        else:
            print(i)