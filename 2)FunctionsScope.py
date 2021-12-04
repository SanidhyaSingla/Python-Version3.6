rainfall = [68, 58, 0, 99, 200, 39, 73, 43, 68, 0, 19]
location = 'Melbourne'

def neat_rainfall(value):
    day = 1
    for values in value:
        print('Day', day, ':', values)
        day +=1

def rainfall_average(value):
    import math
    return math.fsum(value) / len(rainfall)

def location_change(new_location):
    global location
    location = new_location
    new_location = 'Las Vegas'
    print('The new location is', location)

print (neat_rainfall(rainfall))
print(rainfall_average(rainfall))
print(location)
location_change('New Pork')
print(location)