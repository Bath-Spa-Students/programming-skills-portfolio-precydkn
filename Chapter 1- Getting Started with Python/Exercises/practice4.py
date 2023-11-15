# Q4: Compute the area of a triangle.

# Telling the user to input the needed for solving the area of a triangle.
print("Input the height and base of the triangle to compute for its area.")

# function for getting the height, base, and area of a triangle.
height= float(input("Height: ")) # gets user input for the height
base= float(input("Base: ")) # gets user input for the base
area= height*base / 2 # formula for calculating the area of a triangle
print("The area of the triangle is ", area) # displays the answer