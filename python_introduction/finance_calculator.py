monthly_income = int(input("Enter your monthly income:"))
monthly_expense = int(input("Enter your monthly expenses:"))
monthly_savings = income - expense
projected_savings = int(savings * 12 + (savings * 12 * 0.05))
print("Your monthly savings are $",savings)
print("Projected savings after one year, with interest, is: $",projected_savings)
