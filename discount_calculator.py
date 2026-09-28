#Asks for age and ticket price from user
age = int(input("Enter your age: "))
ticketprice = float(input("Enter your ticket price: "))

#If statement to make sure age and ticket price input are valid and non-negative
if age >= 0 and age <= 150 and ticketprice >= 0: 
    if age <= 12:
        discount = 0.5 #Children: 50% discount
        category = "Children"
    elif age <= 17:
        discount = 0.25 #Teenager:25% discount
        category = "Teenagers"
    else:
        discount = 0 #Adults: No discount
        category = "Adults"
    finalprice = ticketprice - ticketprice * discount

#Displays discount category, discount percentage, and final price
    print(f"You are eligible for the {category} discount: {int(discount * 100)}%")
    print(f"Your final ticket price: RM{finalprice:.2f}")


#Output message when age and ticket price input are invalid and negative valued
else:
    print("Please enter a valid age or ticket price")
