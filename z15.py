n = int(input())
for i in range(1,n+1):
    dl = 0
    for j in range(2,i):
        if i % j == 0:
            dl += 1
            break
    if dl == 0:
        print(i)

