numbers = [1, 2, 3, 4, 5, [6, 7, 8, 9, 10]]
letters = ['a', 'b', 'c', 'd', 'e']

# Add the lists
mix = numbers + letters
letters += numbers
print(mix)
print(letters)
# Read the index of the lists
print(letters[3])
# Read the index of the nested lists
print(numbers[5][3])
# Change the items into lists and nested lists
letters[4] = 'E'
print(letters)
numbers[5][4] = 100
print(letters)