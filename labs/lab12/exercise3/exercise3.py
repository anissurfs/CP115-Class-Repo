valid_count = 0
total_grade = 0
grade = float(input())

while grade != -1:


    if grade < 0 or grade > 100:
        grade = float(input())
        continue
    valid_count += 1
    total_grade += grade
    grade = float(input())


average = total_grade / valid_count
print(valid_count)
print(f"{average:.2f}")
