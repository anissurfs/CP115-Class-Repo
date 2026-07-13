distance = float(input())
afterMidnight = input()
if distance <= 2:
    fare = ((distance - 2) * 5.2) + 8
else:
    fare = distance * 4
if afterMidnight == "yes":
    fare = fare + 3
print(fare)
