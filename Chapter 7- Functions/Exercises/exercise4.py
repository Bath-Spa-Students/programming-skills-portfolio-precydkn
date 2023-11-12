## Exercise 4:  Large Shirts
'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different message.'''

# the make_shirt function with a default shirt size and message
def make_shirt(shirt_size="large", message="I love Python"):
    summary= f'The shirt is size {shirt_size}, with "{message}" printed on it.\n' # states the user's input on the shirt size and message printed on it
    print(summary) # displays the sentence above

make_shirt() # displays the default shirt size and message

make_shirt(shirt_size="medium") # displays a medium shirt size but with the default message

make_shirt("XL", "Coding is like Math. They're everywhere.") # displays a different shirt size and message