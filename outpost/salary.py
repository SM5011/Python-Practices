employee_id = input("Enter employee's ID: ")
hours_worked = float(input("Enter total worked hours of the month: "))
hourly_rate = float(input("Enter the amount received per hour: "))

weekend_days = 8  
total_hours_worked = hours_worked - (hours_worked/30 * weekend_days)  

final_salary = total_hours_worked * hourly_rate
print(f"Employee ID: {employee_id}")
print(f"Salary for the month: ${final_salary:.2f}")