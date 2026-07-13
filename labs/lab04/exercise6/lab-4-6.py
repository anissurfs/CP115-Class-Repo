minutesBefore = float(input())
membership = input()
if minutesBefore < 0:
    price = 0
else:
    if minutesBefore > 30:
        ticket = 80
    else:
        ticket = 65
    if membership == "yes":
        price = ticket - ticket * 0.15
    else:
        price = ticket
print(price)
