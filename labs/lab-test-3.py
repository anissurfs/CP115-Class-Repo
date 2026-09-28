"""
Programmer: Anis Soleha Binti Salidin@Sallehuddin

Problem Description: You are required to create a Python program that asks the user to enter the
monthly usage and then calculates and displays the amount of the bill to be paid
after receiving the discount.
"""
#Asks user to enter usage value
usage = float(input("Enter usage: ")) 

#Determining discount based on usage
if usage < 50:
    discount = 0
elif usage <= 100:
    discount = 0.05
else:
    discount = 0.2

#Calculates the total bill after determining discount and displays it
print(usage - usage * discount)