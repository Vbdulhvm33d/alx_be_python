#define the basic parameters for annual savings
monthly_income = int(input("Enter your monthly income"))
monthly_expenses = int(input("Enter your total monthly expenses"))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
#output results
print("your monthly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_savings) 