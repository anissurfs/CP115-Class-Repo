print("Input weight")
weight = float(input())
print("Input Ticket Price")
ticketPrice = float(input())
if weight == 0:
    finalPrice = ticketPrice - 10
else:
    if weight <= 15:
        pass
    else:
        exWeight = (weight - 15) * 4
        finalPrice = exWeight + ticketPrice
print(finalPrice)
