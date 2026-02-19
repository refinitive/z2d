for i in range(3):
    print("Hello")

for i in range(3):
    print(i)

for i in range(3):
    print("Loop number:", i)


total = 0

for i in range(5):
    total += 1

print(total)


for i in range(1, 6):
    print(i)


rent = 10000
for year in range(1, 6):
    rent = rent * 1.1
    print("Year", year, "Rent:", rent)


count = 0

while count < 3:
    print("Count is", count)
    count += 1


for i in range(1,11):
    print(i)

for i in range(1,11):
    if i % 2 == 0:
        print(i)


money = 0

while money < 5000:
    money += 500
    print(money)


money = 0
months = 0

while money < 5000:
    money += 500
    months += 1
    print("Money:", money, "Months:", months)


money = 0
months = 0

while money <= 5000:
    money += 500
    months += 1
    print("Money:", money, "Months:", months)


savings = 0

for months in range(1, 11):
    savings += 500
    print("Months:", months, "Savings:", savings)


savings = 0
months = 0

while savings < 5000:
    savings += 500
    savings *= 1.01
    months += 1

    print("Month:", months, "Savings:", round(savings, 2))

print ("Reached 5000 in", months, "months")


money = 0
months = 0
while money < 5000:
    money += 500
    money *= 1.10
    months += 1
print("A months:", months, "final:", round(money, 2))

money = 0
months = 0
while money < 5000:
    money *= 1.10
    money += 500
    months += 1
print("B months:", months, "final:", round(money, 2))
