days = ['monday','tuesday','wednesday','thursday','sunday']

for day in days:
    if days.index(day) == len(days)-1:
        print('I do not go to work on ' + day)
    else:
        print('I go to work on ' + day)