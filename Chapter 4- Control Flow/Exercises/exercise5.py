## Exercise 5: Favorite Fruit 
'''Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
•   Make a list of your three favorite fruits and call it favorite_fruits.
•   Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, 
    the if block should print a statement, such as You really like bananas!'''

# a list of fruit names
favorite_fruits = ["orange" , "mango" , "grapes"]

# if statements to check whether a fruit name is in the list
if "orange" in favorite_fruits: 
    print("You really like oranges!") # displays a message about the orange because it's part of the list

if "banana" in favorite_fruits:
    print("You really like bananas!") # displays nothing because banana is not part of the list

if "grapes" in favorite_fruits: 
    print("You really like grapes!") # displays a message about the grapes because it's part of the list

if "mango" in favorite_fruits: 
    print("You really like mangoes!") # displays a message about the mangoes because it's part of the list

if "strawberry" in favorite_fruits:
    print("You really like strawberries!") # displays nothing because strawberry is not part of the list
