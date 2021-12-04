print('Enter the number of days:')
days = int(input())

years = days // 365
weeks = (days%365) // 7
remaining_days = days - 365*years - weeks*7

print('So, the days in years will be:', years, 'years, ', remaining_days, 'days and ', weeks, 'weeks')