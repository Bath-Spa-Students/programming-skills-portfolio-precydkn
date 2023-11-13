# calculating the area of a circle with user input for the values of the circle
from math import pi # getting data of the value of pi
radius = float(input("Input the radius of the circle: ")) # user input for the radius of the circle
area = pi * (radius**2) # formula for computing the area of circle
print("The area of the circle is: %.2f " % area) # displays the answer
