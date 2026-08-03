import math
print ("Radius:")
radius = int(input())
area = math.pi * math.pow(radius,2)
circumference = 2 * math.pi * radius
print (f"Area: {round(area,2)}")
print (f"Circumference: {round(circumference,2)}")