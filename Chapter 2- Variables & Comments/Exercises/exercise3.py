""" Exercise 3: Tidy up the code to make it easier to understand. Use a variable to represent a person’s name, and include some 
whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least 
once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping 
functions, lstrip(), rstrip(), and strip()."""

# storing a name with a space at the start and the end in a variable
name = "\tPrecy\n"
print(name) # displays the name with spaces at the start and end of it
print(name.lstrip()) # displays the name without the space at the start using lstrip
print(name.rstrip()) # displays the name without the space at the end using rstrip
print(name.strip()) # displays the name without the spaces at the start and the end using strip
