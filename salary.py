import sys
if len(sys.argv) == 2:
    salary = float(sys.argv[1])
else:
    print("No input provided. Using default salary: 50000")
    salary = 50000.0
bonus = salary * 0.10
total_salary = salary + bonus
print("Bonus Amount:", bonus)
print("Total Salary after adding Bonus:", total_salary)
