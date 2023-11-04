## Exercise 4: Deli 
'''Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.'''

sandwich_orders = ["grilled cheese", "club", "ham and cheese"] # a list of names of sandwiches
finished_sandwiches = [] # an empty list to put the values from the list above later

while sandwich_orders:
    sandwich = sandwich_orders.pop(0) # the first sandwich in the sandwich_orders list is removed
    print(f"Your {sandwich} sandwich is being made.")
    finished_sandwiches.append(sandwich) # every removed sandwich from sandwich_orders is added to finished_sandwiches

print("\n") # just a space between the sandwich orders and finished sanwiches displays
# a for loop displaying the each sandwich from finished_sandwiches
for x in finished_sandwiches:
    print(f"Here is your {x} sandwich.") 