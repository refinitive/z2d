print("Net Rental Yield Calculator")
print("---------------------------")

# Get inputs
try:
    purchase_price = float(input("Enter purchase price: "))
    monthly_rent = float(input("Enter monthly rent: "))
    monthly_expenses = float(input("Enter monthly operating expenses: "))
except ValueError:
    print(("Invalid input. Please enter numbers only"))
    exit()

# Calculate
annual_rent = monthly_rent * 12
annual_expenses = monthly_expenses * 12
net_operating_income = annual_rent - annual_expenses
yield_percentage = (net_operating_income / purchase_price) * 100

# Output
print("\nResults")
print("Annual Rent:", annual_rent)
print("Annual Expenses:", annual_expenses)
print("Net Operating Income:", net_operating_income)
print("Net Yield:", round(yield_percentage, 2), "%")

# Rating
if yield_percentage > 10:
    print("Rating: Strong deal")
elif yield_percentage >= 7:
    print("Rating: Moderate deal")
else:
    print("Rating: Weak deal")

# End
print("---------------------------")