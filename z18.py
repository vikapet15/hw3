x = int(input())
k = 0
a = 1
while a * a <= x:
    ost = x - a*a
    b = int(ost ** 0.5)
    if b > 0 and b*b == ost:
        if a <= b:
            k += 1
    a += 1
print(k)

