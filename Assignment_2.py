num = int(input('Enter the number: '))

flag = False
i = 2

while i <= num/2:
    if num%i == 0:
        flag = True
        break
    else:
        i += 1

if flag == True:
    print(num, 'is not a prime number.')
else:
    print(num, 'is a prime number.')