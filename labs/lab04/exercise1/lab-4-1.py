kwh = int(input())
if kwh <= 100:
    chargePrice = 0.3
else:
    if kwh <= 200:
        chargePrice = 0.5
    else:
        chargePrice = 0.75
totalBill = kwh * chargePrice
print(totalBill)
