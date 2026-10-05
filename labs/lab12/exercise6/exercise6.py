a = int(input())
b = int(input())
overtake_round = 0
rounds = 0

while a != -1 or b != -1:

    rounds += 1

    if b > a:
        overtake_round = rounds
        break

    a = int(input())
    if a == -1:
        break
    b = int(input())
    if b == -1:
        break



print(overtake_round)
