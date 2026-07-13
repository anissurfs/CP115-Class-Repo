weight = float(input())
ticketPrice = float(input())
if weight == 0:
    finalPrice = ticketPrice - 10
else:
    if weight <= 15:
        finalPrice = ticketPrice
    else:
        exWeight = (weight - 15) * 4
        finalPrice = exWeight + ticketPrice
print(finalPrice)
