print ("Your name:")
name = str(input())
print ("Price:")
price = int(input())
print ("Quantity:")
quantity = int(input())
tax_rate = 0.06
subtotal = price * quantity
tax_amount = subtotal * tax_rate
total_cost = subtotal + tax_amount
print (f"Subtotal is {subtotal}, tax amount is {tax_amount}, and total cost is {total_cost}")