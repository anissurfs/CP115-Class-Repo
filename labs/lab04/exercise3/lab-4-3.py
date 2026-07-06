hours = float(input())
if hours <= 2:
    charge = 0
else:
    if hours <= 5:
        charge = 5
    else:
        charge = 3
parkingFee = hours * charge
if parkingFee > 30:
    parkingFee = 30
print(parkingFee)
