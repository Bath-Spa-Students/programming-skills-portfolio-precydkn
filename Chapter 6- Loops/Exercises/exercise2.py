## Exercise 2: Movie Tickets
'''A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
age, and then tell them the cost of their movie ticket.'''

# a while loop that terminates once the user input is "exit"
while True:
    age = input('Enter "exit" to finish. Enter your age: ') # user input of the string above
    if age == "exit":
        break
    age = int(age) # turns age into an integer so the computer can read the user input and run the program
    
    if age < 3:
        print("Your ticket is free!\n")
    elif age < 12:
        print("Your ticket costs $10.\n")
    else:
        print("Your ticket costs $15.\n")
print("\nEnjoy the movie!")