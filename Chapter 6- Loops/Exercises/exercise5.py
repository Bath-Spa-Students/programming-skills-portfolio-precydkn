## Exercise 5: No Pastrami :ballot_box_with_check:
'''Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop 
to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.'''

sandwich_orders = ["pastrami", "grilled cheese", "club", "pastrami", "pastrami", "ham and cheese"] # list of sandwich names from Exercise 4 but with 'pastrami' added 3 times
finished_sandwiches = [] # an empty list to put the values from the list above later

print("We are out of pastrami sandwich at this time, sorry.\n")
# a while loop that runs until all "pastrami" sandwiches are removed from the sandwich_orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"Your {sandwich} sandwich is being made.")
    finished_sandwiches.append(sandwich)

print("\n") #just a space between the sandwich orders and finished sanwiches displays
for x in finished_sandwiches:
    print(f"Here's your {x} sandwich.")