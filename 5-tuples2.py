numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
letters = ('a', 'b', 'c', 'd')

# slicing of tuples
print(numbers[0:9:8])
odd_nums = print(numbers[0::2])
even_nums = print(numbers[1::2])

# iteration with tuples
# This is another way to change the value of tuples without changing them in real
for n in numbers:
    print(n ** 2) # Created squares without changing the value of the tuple

# function with tuples
def area_circumference_of_circle(r):
    import math
    return (math.pi * r ** numbers[1], numbers[1] * math.pi * r)
print(area_circumference_of_circle(34))
# common errors with tuples (assignment, iteration)
print('There are no other errors in tuples other than assigning of any other value in tuples, which is wrong and can be'
      ' done in lists other than tuples. AND you also can\'t iterate anything in tuples. *NOTE*: Both these things '
      'can\'t be done because TUPLES ARE IMMUTABLE.')
