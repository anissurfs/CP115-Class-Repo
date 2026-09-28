num_rounds = int(input())
final_score = 0
for rounds_processed in range(1, num_rounds+1):
    score = float(input())

    if score > 100:
        final_score += score *1.2
    else: 
        final_score += score
'''
    if score > 100:
        score = score + (score * 0.2)

    final_score += score
    '''

print(f"{final_score:.1f}")
print(rounds_processed)
2