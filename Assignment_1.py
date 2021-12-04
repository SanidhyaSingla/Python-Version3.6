p = float(input('Enter the principle: '))
r = float(input('Enter the rate of interest: '))
t = float(input('Enter the duration of keeping the money: '))
print('Option A: Annually')
print('Option B: Half-Yearly')
print('Option C: Quarterly')
o = input('Select your option in a letter: ')
f = 0.5

si = p*r*t/100

if o == 'A' or 'a':
    f = 1
elif o == 'b' or 'B':
    f = 0.5
elif o == 'c' or 'C':
    f = 0.25

r = r*f
t = t/f
print(r)
print(t)

ci = "{:.2f}".format(((p*((1+(r/100))**t)) - p))

print('Simple Interest: ₹', si)
print('Compound Interest: ₹', ci)

