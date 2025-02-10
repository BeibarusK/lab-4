import math
#1
def from_degree_to_radian(degree):
    return math.radians(degree)
print(from_degree_to_radian(15))

#2
def area_of_trapezoid(height, first_value,second_value):
    return ((first_value+second_value)*height)/2
print(area_of_trapezoid(5,5,6))

#3
def area_of_regular_polygon(number_of_sides,length):
    perimetr=length*number_of_sides
    radians = from_degree_to_radian(180/number_of_sides)
    apothem=length/(2*math.tan(radians))
    return int(perimetr*0.5*apothem)
print(area_of_regular_polygon(4,25))

#4
def area_of_parallelogram(length,height):
    return length*height
print(area_of_parallelogram(5,6))