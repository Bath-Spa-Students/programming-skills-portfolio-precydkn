## Exercise 5: Cities
'''Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
such as Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.'''

# a function that accepts the name of a city and its country, with country having a default value
def describe_city(city, country="the Philippines"):
    result= f"{city} is in {country}.\n" # states the city and its country
    print(result) # displays the sentence above

describe_city("Manila") # giving a city name with default country
describe_city("Baguio") # giving a city name with default country
describe_city("Ras Al Khaimah", "UAE") # giving a city and country name