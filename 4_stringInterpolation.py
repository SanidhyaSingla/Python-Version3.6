person = 'Mr.Bob Bobington'
pet_name = 'Bobby'
pet_type = 'dog'

print(person, 'has a', pet_type, 'and his name is', pet_name)

print(f'{person} has a {pet_type} and his name is {pet_name}')
print('{} has a {} and his name is {}'.format(person, pet_type, pet_name))
print('%s has a %s and his name is %s' % (person, pet_type, pet_name))