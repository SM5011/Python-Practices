def run(day):
    if day == 'friday':
        print(day,'Today is holyday')
    else :
        print(day,'working day')

days = ['satutday', 'sunday','tuesday','thusday','friday']
days.insert(days.index('sunday')+1,'monday')
days.insert(days.index('tuesday')+1,'wednesday')
print(*days)

for day in days:
    run(day)