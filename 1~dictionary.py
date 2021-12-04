# create a dictionary in 2 different ways
scores = dict(
    Dudley=20,
    Ronald=23
)

nicknames = {'Dudley': 'Dudders', 'Ronald': 'Ron'}
# print dictionary
print(scores)
print(nicknames)

# read a specific value from a dictionary
print(scores['Ronald'])
scores['Hermy'] = 22
scores['Hermy'] += 3
print(scores)
