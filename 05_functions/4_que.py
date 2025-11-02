import math

def cirlce_ststs(radius):
    area = math.pi * radius ** 2
    circ = 2 * math.pi * radius
    return area , circ 

a, c = cirlce_ststs(2)

print("area is : {:.2f}  circumferace is : {:.2f}".format(a, c))