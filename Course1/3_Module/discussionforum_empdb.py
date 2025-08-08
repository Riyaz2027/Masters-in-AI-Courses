# List 1: HR department
hr_employees = ("Alice", "Aman", "Clara")

# List 2: IT department
it_employees = ("David", "Mickey", "Farhan")

# List 3: Finance department
finance_employees = ("George", "Jack", "Jill")

# Combine all into one tuple of tuples
employee_database = (hr_employees, it_employees, finance_employees)

# Print the database
print("Employee Database:")

[print(f"Department {dept_index}: {dept}") for dept_index, dept in enumerate(employee_database, start=1)]

# input asking y or no
user_input = input("Do you want to add a new employee? (y/n): ").strip().lower()
#if user_input == y then print "You have chosen to add a new employee."
if user_input.lower() == 'y':
    print(user_input)