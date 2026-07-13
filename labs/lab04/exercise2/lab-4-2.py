income = float(input())
if income >= 50000:
    if income >= 100000:
        totalTax = 500 + income - 100000 * 0.02
    else:
        totalTax = income - 50000 * 0.01
else:
    totalTax = 0
print(totalTax)
