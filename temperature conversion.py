"""
celsius_temps = [0,10,20,30,40,50]
fahrenheit_temp = []

for temp in celsius_temps:
    fahrenheit_temp.append((temp*9/5)+32)
print(fahrenheit_temp)
"""
celsius_temps = [0, 10, 20, 30, 40, 50]

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Use map to apply the conversion function to each temperature
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))

print(fahrenheit_temps)

