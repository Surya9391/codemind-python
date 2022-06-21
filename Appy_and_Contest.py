n = int(input())
while(n):
    N, A, B, K = map(int, input().split())
    a = N//A
    b = N//B
    c = N//(A*B)
    if(a+b)-c>=K:
        print('Win')
    else:
        print('Lose')