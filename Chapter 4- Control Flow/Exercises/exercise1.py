## Exercise 1:  Alien Colors #1 
'''Imagine an alien was just shot down in a game. 
Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•   Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
•   Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)'''

## a passing program for when the alien is green
alien_color = "green" or "yellow" or "red" # assigning the alien colors

# if statement about the points earned if the alien color is green
if alien_color == "green":
    print("You have just earned 5 points!") # displays the earned points if the alian color is green

## a failed program for when the alien is not green
alien_color = "yellow" or "red" # assigning the alien colors

# if statement about the points earned if the alien is green
if alien_color == "green":
    print("You have just earned 5 points!") # displays nothing because the alien is not green
