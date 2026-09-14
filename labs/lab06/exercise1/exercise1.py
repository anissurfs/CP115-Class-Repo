#Setting the item prices
coffeeP = 3.50
muffinP = 2.10
waterP = 1.05

coffeeQ = int(input("Coffee Quantity: "))
muffinQ = int(input("Coffee Quantity: "))
waterQ = int(input("Coffee Quantity: "))
coffeeT = coffeeP * coffeeQ
muffinT = muffinP * muffinQ
waterT = waterP * waterQ
subtotal = coffeeT + muffinT + waterT
tax = subtotal * 0.06
totalP = subtotal + tax
print(coffeeT)
print(f"========== RECEIPT ==========\nItem\tPrice\tQty\tTotal\nCoffee\t${coffeeP}\t{coffeeQ}\t${round(coffeeT,2)}\nMuffin\t${muffinP}\t{muffinQ}\t${round(muffinT,2)}\nWater\t${waterP}\t{waterQ}\t${round(waterT,2)}\n-----------------------------\nSubtotal\t\t${round(subtotal,2)}\nTax (6%)\t\t${round(tax,2)}\nTotal\t\t\t${round(totalP,2)}\n=============================")