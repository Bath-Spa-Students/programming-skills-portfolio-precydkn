## Exercise 3: T-Shirt
'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
arguments to make a shirt. Call the function a second time using keyword arguments.'''

# a function that accepts shirt size and message to print on the shirt
def make_shirt(shirt_size, message):
    summary= f'The shirt is size {shirt_size}, with "{message}" printed on it.\n' # states the user's input on the shirt size and message printed on it
    print(summary) # displays the sentence above

# calling the function using positional arguments (shirt_size, message)
make_shirt("small", "Code Lab is cool!")

# calling the function using keyword arguments (variable = "value")
make_shirt(message="Coding is fun :)", shirt_size="XS")