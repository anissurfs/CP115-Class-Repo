number = int(input())
count = 0
biggest_jump = 0
jump = 0

while number != 0:
    count += 1
    current_number = number
    number = int(input())

    jump = current_number - number
    if jump > biggest_jump:
        biggest_jump = jump



print(count)
print(biggest_jump)
