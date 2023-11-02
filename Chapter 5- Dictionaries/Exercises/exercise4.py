## Exercise 4: Rivers
'''Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''

# a dictionary of major rivers and their country
majorRivers = {'Mississippi' : 'United States',
               'Ob' : 'Russia',
               'Mackenzie' : 'Canada'}

# using a loop to print a sentence about each river
for river, country in majorRivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# just a space between the the sentences above and the next information below them
print("\n")

# using a loop to print the rivers included in the dictionary
for river, country in majorRivers.items():
    print(f"{river.title()}")

# just a space between the river and countries
print("\n")

# using a loop to print the countries included in the dictionary
for river, country in majorRivers.items():
    print(f"{country.title()}")