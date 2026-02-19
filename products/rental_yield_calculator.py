print("Rental Yield Calculator")
print("-----------------------")

# Get inputs
purchase_price = float(input("Enter purchase price: "))
monthly_rent = float(input("Enter monthly rent: "))

# Calculate
annual_rent = monthly_rent * 12
yield_percentage = (annual_rent / purchase_price) * 100

# Output
print("\nResults")
print("Annual Rent:", annual_rent)
print("Gross Yield:", round(yield_percentage, 2), "%")

# Rating
if yield_percentage > 10:
    print("Rating: Strong deal")
elif yield_percentage >= 7:
    print("Rating: Moderate deal")
else:
    print("Rating: Weak deal")
    