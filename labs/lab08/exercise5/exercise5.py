main_course = input()
drink = input()
dessert = input()

if main_course == "Chicken":
    main_price = 10
elif main_course == "Beef":
    main_price = 12
else:
    main_price = 11

if drink == "Soft Drink":
    drink_price = 2
else:
    drink_price = 3

if dessert == "Ice Cream":
    dessert_price = 4
else:
    dessert_price = 5

food_price = main_price + dessert_price + drink_price
final_bill = food_price + (food_price *0.1)

print(f"{final_bill:.2f}")
