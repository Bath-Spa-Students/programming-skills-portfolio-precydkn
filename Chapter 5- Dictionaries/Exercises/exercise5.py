## Exercise 5: Pets 
'''Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet'''

## make dictionaries about different pets
# dictionary of pet1 and information about them
pet1 = {'Animal' : 'Cat',
        'Name' : 'Krunch',
        'Owner' : 'John',
        'Sex' : 'Male',
        'Favorite food' : 'Dreamies Treats'}

# dictionary of pet2 and information about them
pet2 = {'Animal' : 'Bear',
        'Name' : 'Pooh',
        'Owner' : 'Christopher',
        'Sex' : 'Male',
        'Favorite food' : 'Honey'}

# dictionary of pet2 and information about them
pet3 = {'Animal' : 'Pig',
        'Name' : 'Piglet',
        'Owner' : 'Robin',
        'Sex' : 'Male',
        'Favorite food' : 'Acorns'}

# a list called pets to store all the dictionaries above
pets = [pet1, pet2, pet3]

for pet1 in pets:
    print(f"\nAbout {pet1['Name'].title()}")
    for key, value in pet1.items():
        print(f"\t{key} : {value}")