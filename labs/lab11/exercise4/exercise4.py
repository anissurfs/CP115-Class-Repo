sales = int(input())
record_days = 1
count = 0

while sales != 0:
    count += 1

    newsales = int(input())

    if newsales > sales:
        record_days += 1

    sales = newsales

print(count)
print(record_days)
