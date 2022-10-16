money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

while True:
    if spend <= money_capital:
        month += 1
        money_capital += salary - spend
        spend += spend * increase
    else:
        break

print(month)
