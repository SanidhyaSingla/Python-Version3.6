a = [2, 4, 8, 9, 11, 13, 14]
b = len(a)

even = []
odd = []

for i in range(b):
    if a [i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

print('Even Numbers:', even)
print('Odd Numbers:', odd)