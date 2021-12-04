mesi = ['January',       # Mesi is months but in italian
        'February',
        'Marchos',
        'April',
        'Mayos',
        'Juny',
        'Juli',
        'Augy',
        'Septagonember',
        'Octogonember',
        'Novetel',
        'Decidember']

# 1. Lambda function calculating kinetic energy Ke = (m*v**2)/2
kinetic_energy = lambda m, v: (m*v**2)/2
print('Kinetic Energy:', kinetic_energy(50, 100), 'Joules')

# 2. Lambda function calculating energy E = Mc**2
energy = lambda m, c: m*c**2
print('Energy:', energy(100, 56), 'Joules')

# 3. Lambda function calculating gravitational force F = G*m1*m2/r**2
gforceChoke = lambda m1, m2 = 5.972 * 10 ** 24, r = 6371000: 6.67408*10**-11*m1*m2/r**2
print('Gravitational Force:', gforceChoke(44, 11, 34), 'Newtons')

# 4. Lambda function calculating abbreviation(JAN, FEB, etc.) for each month from the list
abv_mesi = list(map(lambda mesi: mesi[:3].upper(), mesi))

print(abv_mesi)
print(type(abv_mesi))
print(type(energy))