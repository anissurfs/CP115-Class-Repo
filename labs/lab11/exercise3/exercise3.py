number = int(input())
count = 0
biggest_jump = 0
jump = 0

while number != 0:
    count += 1

    newnumber = int(input())

    jump = newnumber - number

    if jump > biggest_jump:
        biggest_jump = jump

    number = newnumber

print(count)
print(biggest_jump)
