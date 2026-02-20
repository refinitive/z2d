def calculate_gross_yield(purchase_price, monthly_rent):
    annual_rent = monthly_rent * 12
    gross_yield = (annual_rent / purchase_price) * 100
    return gross_yield

price = 2000000
rent = 15000

result = calculate_gross_yield(price, rent)

print(f"Gross Yield: {result:.2f}%")


def calculate_net_yield(purchase_price, monthly_rent, monthly_expenses):
    annual_rent = monthly_rent * 12
    annual_expenses = monthly_expenses * 12
    net_income = annual_rent - annual_expenses
    net_yield = (net_income / purchase_price) * 100
    return net_yield

expenses = 3000

net_result = calculate_net_yield(price, rent, expenses)

print(f"Net Yield: {net_result:.2f}%")
