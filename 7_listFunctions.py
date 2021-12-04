# List functions:-
'''
These functions are for console.
len(list)      # returns the number of items in the list
max(list)      # returns the highest number or the last string
min(list)      # returns the lowest number or the lowest string
sum(list)      # returns the sum of all the numbers if the list is made up of numbers of floats(decimals)
sorted(list)   # permanently rearranges the list from lowest to highest
'''

rainfall = [68, 58, 0, 99, 200, 39, 73, 43, 68, 0, 19]

min_rainfall = min(rainfall)
print('Minimum rainfall :', min_rainfall)

max_rainfall = max(rainfall)
print('Maximum rainfall :', max_rainfall)

average_rainfall = sum(rainfall) / len(rainfall)
print('Average rainfall :', average_rainfall)

sorted_rainfall = sorted(rainfall)
print('Sorted rainfall :', sorted_rainfall)
Sorted_rainfall = sorted(rainfall, reverse=True)
print('                :', Sorted_rainfall)