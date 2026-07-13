scoreA = int(input())
scoreB = int(input())
pointsA = 0
pointsB = 0
if scoreA == scoreB:
    pointsA = 1
    pointsB = 1
else:
    if scoreA > scoreB:
        if scoreB == 0:
            pointsA = 4
        else:
            pointsA = 3
    else:
        if scoreA == 0:
            pointsB = 4
        else:
            pointsB = 3
print(pointsA)
print(pointsB)
