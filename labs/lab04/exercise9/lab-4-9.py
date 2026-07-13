gb = float(input())
bill1 = 10 + gb
if gb > 20:
    bill2 = 25 + ((gb - 20) * 3)
else:
    bill2 = 25
if bill1 <= bill2:
    bill = bill1
else:
    bill = bill2
print(bill)
