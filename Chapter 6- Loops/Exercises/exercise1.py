## Exercise 1: Pizza Toppings
'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
As they enter each topping, print a message saying you’ll add that topping to their pizza.'''

# a while loop that terminates once user inputs quit
toppings = (input("What toppings do you want to put on your pizza? \n  -> ")) # takes user input about the toppings they want on their pizza
while toppings != "quit":
    print(f"\n{toppings} will be added to your pizza :)") # tells the user that their chosen topping will be added to their pizza
    toppings = (input('Any more you want to add to your pizza? Otherwise, enter "quit" if you are already satisfied with your pizza. \n  -> ')) #asks user again and tells how to stop the program
print("\nEnjoy your pizza!")