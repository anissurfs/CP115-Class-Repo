# Lab 07 scratch file
# Use this file to try out the code from the lab as you follow along.
# Test addition and subtraction

result1 = 25 + 15
result2 = 100 - 25
print(f"25 + 15 = {result1}")
print(f"100 - 25 = {result2}")
# Test multiplication and division
result3 = 8 * 7
result4 = 20 / 4
print(f"8 * 7 = {result3}")
print(f"20 / 4 = {result4}")
# Test floor division, modulus, and powers
result5 = 17 // 5
result6 = 17 % 5
result7 = 3 ** 4
print(f"17 // 5 = {result5}")
print(f"17 % 5 = {result6}")
print(f"3 ** 4 = {result7}") 


# Test division - always returns float
division = 10 / 2
print(f"10 / 2 = {division} (type: {type(division)})")

# Test floor division - returns int when both operands are int
floor_div = 10 // 3
print(f"10 // 3 = {floor_div} (type: {type(floor_div)})")

# Test modulus - returns int when both operands are int
modulus = 17 % 5
print(f"17 % 5 = {modulus} (type: {type(modulus)})")

# Test exponentiation - returns int when both operands are int
power = 2 ** 3
print(f"2 ** 3 = {power} (type: {type(power)})")

# Test mixing int and float in different operations
mixed_division = 15.0 / 4        # float / int = float
mixed_floor = 15.0 // 4          # float // int = float
mixed_modulus = 17.0 % 5         # float % int = float
mixed_power = 2.0 ** 3           # float ** int = float

print(f"15.0 / 4 = {mixed_division} (type: {type(mixed_division)})")
print(f"15.0 // 4 = {mixed_floor} (type: {type(mixed_floor)})")
print(f"17.0 % 5 = {mixed_modulus} (type: {type(mixed_modulus)})")
print(f"2.0 ** 3 = {mixed_power} (type: {type(mixed_power)})")

# Test assignment operators
score = 100
print(f"Starting score: {score}")

score += 10     # Add 10
print(f"After += 10: {score}")

score -= 5      # Subtract 5
print(f"After -= 5: {score}")

score *= 2      # Multiply by 2
print(f"After *= 2: {score}")

score //= 3     # Floor division by 3
print(f"After //= 3: {score}")

score %= 15     # Modulus by 15
print(f"After %= 15: {score}")

score **= 2     # Square it
print(f"After **= 2: {score}")

import math
import random

# Using the modules
result = math.sqrt(25)
number = random.randint(1, 10)