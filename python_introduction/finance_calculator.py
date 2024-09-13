income = int(input("Enter your monthly income:"))
expense = int(input("Enter your monthly expenses:"))
savings = income - expense
projected_savings = int(savings * 12 + (savings * 12 * 0.05))
print("Your monthly savings are $",savings)
print("Projected savings after one year, with interest, is: $",projected_savings)
