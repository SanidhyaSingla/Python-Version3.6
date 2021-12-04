# Question: Write a function in one line to get the calorific value of a fuel giving the fuel burnt and energy produced

calorific_value = lambda f, e: e/f
print('The calorific value of the fuel is', calorific_value(2, 180), 'KiloJoules')
print('*This function returns the value of calorific value on the bases of amount of the fuel burnt and heat energy produced*')
