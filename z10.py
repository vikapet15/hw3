k = 0
pred = 0
while (tek := float(input())) != 0:
    if tek < pred:
        k += 1
    pred = tek
print(k)
