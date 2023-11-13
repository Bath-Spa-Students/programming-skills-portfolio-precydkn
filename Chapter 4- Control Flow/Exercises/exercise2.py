## Exercise 2: Alien Colors #2 
"""Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
•   If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
•   If the alien’s color isn’t green, print a statement that the player just earned 10 points.
•   Write one version of this program that runs the if block and another that runs the else block."""

# assigning a color to the alien
alien_color = "yellow"

# if-else statement about the points earned based on the color of the alien
if alien_color == "green":
    print("Green Alien shot. You earn 5 points!") # displays 5 points earned if the alien is green
else:
    print("Yellow Alien shot. You earn 10 points!") # displays 10 points earned if the alien is yellow
