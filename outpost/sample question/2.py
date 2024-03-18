# Answer to question no. 2.1
temperatures = [22, 18, 25, 20, 17, 23, 21]
print('Solution 1:-')
print(temperatures) 

# Answer to question no. 2.2

lowest_index = temperatures.index(min(temperatures))
highest_index = temperatures.index(max(temperatures))

temperatures[lowest_index], temperatures[highest_index] = temperatures[highest_index], temperatures[lowest_index]

# Answer to question no. 2.3
print('\nSolution 3:-')
print(temperatures)

