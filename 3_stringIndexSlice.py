colour = input('Please enter hex colour value:')
r = colour[0:2]
g = colour[2:4]
b = colour[4:6]

print('r:', r)
print('g:', g)
print('b:', b)

r = int(r, 16)
g = int(g, 16)
b = int(b, 16)

print('r:', r)
print('g:', g)
print('b:', b)