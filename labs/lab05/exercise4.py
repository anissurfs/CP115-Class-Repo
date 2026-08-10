name = str(input("Your name: "))
price = int(input("Price: "))
quantity = int(input("Quantity: "))
tax_rate = 0.06
subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount
print (f"Subtotal: {subtotal}\nTax amount:{tax_amount}\nTotal cost: {total_cost}")