import math

def calculate(radius):
    area=math.pi * radius ** 2
    circum = 2 * math.pi * radius

    return area,circum

area, circum = calculate(5)
print(round(area, 2),round(circum,2))