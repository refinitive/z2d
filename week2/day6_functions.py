def calculate_gross_yield(purchase_price, monthly_rent):
    annual_rent = monthly_rent * 12
    gross_yield = (annual_rent / purchase_price) * 100
    return gross_yield

def calculate_net_yield(purchase_price, monthly_rent, monthly_expenses):
    annual_rent = monthly_rent * 12
    annual_expenses = monthly_expenses * 12
    net_income = annual_rent - annual_expenses
    net_yield = (net_income / purchase_price) * 100
    return net_yield

def main():
    price = float(input("Enter purchase price: "))
    rent = float(input("Enter monthly rental income: "))
    expenses = float(input("Enter monthly expenses: "))
    
    gross = calculate_gross_yield(price, rent)
    net = calculate_net_yield(price, rent, expenses)
    
    print(f"Gross Yield: {gross:.2f}%")
    print(f"Net Yield: {net:.2f}%")

if __name__ == "__main__":
    main()
