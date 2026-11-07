N,K,R = map(int,input().split())
cnt_d = 1
while N < R:
    N *= (1 + K/100)
    cnt_d += 1
if N >= R:
    print(cnt_d)
