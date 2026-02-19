age = 34
has_license = True

if age >= 18 and has_license:
    print("Can drive")
else:
    print("Cannot drive")


temperature = -10

if temperature >30:
    print("Hot")
elif temperature >= 15:
    print("Moderate")
elif temperature >= -9:
    print("Cold")
else:
    print("Freezing")


purchase_price = 2000000
monthly_rent = 18000

annual_rent = monthly_rent * 12
print(annual_rent)

yield_percentage = (annual_rent / purchase_price) * 100
print(yield_percentage)

if yield_percentage > 8:
    print("Strong deal")
elif yield_percentage >= 6:
    print("Decent deal")
else:
    print("Weak deal")