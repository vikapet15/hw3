
a = int(input())
ak = a ** 0.5
while int(ak) != ak:
    print('не является')
    a = int(input())
    ak = a ** 0.5
if int(ak) == ak:
    print('является')


