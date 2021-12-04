# create tuples
numeros = (1, 2, 3, 4, 5, 6)
mush = (1.43, 'Badalalalalala', 5678)

# create nested or 2D tuples
dim2tuplos = (('Mcqueen', 'Mater'), ('Finn Mcmissile', 'Light Blue'))

# access items from tuples and nested tuples
print(numeros[3])
print(mush[1])
print(dim2tuplos[1])
print(dim2tuplos[1][0])

# pack and unpack tuples
pack_tuplos = 2, 'Fish', 9
print(pack_tuplos)
a, b, c = pack_tuplos
print(a)
print(b)
print(c)
print(pack_tuplos)