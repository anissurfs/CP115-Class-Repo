score = int(input())
total_a = 0
total_b = 0
current_score = 0
while score != -1:
    current_score += 1

    if (current_score % 2) ==0:
        total_b += score
    else:
        total_a += score

if total_a == total_b:
    winner = "Tie"
elif total_a > total_b:
    winner = "A"
else:
    winner = "B"
print(total_a)
print(total_b)
print(winner)