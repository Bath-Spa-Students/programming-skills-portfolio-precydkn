## Exercise 4: Stages of Life 
'''Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
•   If the person is less than 2 years old, print a message that the person is a baby.
•   If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
•   If the person is at least 4 years old but less than 13, print a message that the person is a kid.
•   If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
•   If the person is at least 20 years old but less than 65, print a message that the person is an adult.
•   If the person is age 65 or older, print a message that the person is an elder.'''

# assigning an age
age = 44

print(f"The age of the person is {age}") # shows the assigned age

#if-elif-else statement to know what stage in life the person is based on the assigned age
if age < 2:
    print("The person is a baby.") # displays the baby stage
elif age < 4:
    print("The person is a toddler.") # displays the toddler stage
elif age < 13:
    print("The person is a kid.") # displays the kid stage
elif age < 20:
    print("The person is a teenager.") # displays the teenager stage
elif age < 65:
    print("The person is a adult.") # displays the adult stage
else:
    print("The person is a elder.") # displays the elder stage
