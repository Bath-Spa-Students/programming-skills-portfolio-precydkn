## Exercise 3: Glossary 2
'''Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.'''

# same glossary from exercise 2 but with additional 5 words
glossary = {'Algorithm' : 'are sets of steps that are followed to perform a task.', 
            'Slicing' : 'getting a part or a section of elements from a list.',
            'Index' : 'is the position of the values in a list.',
            'Variable' : 'is where values are stored.',
            'Floats' : 'are positive and negative decimal numbers.',
            'Strings' : 'are characters enclosed in single or double quotation marks.',
            'Integers' : 'are positive and negative whole numbers.',
            'Comments' : 'are things written to guide the coders about their programs. These are not read and run by the computer as they start with a hashtag or are enclosed in quotation marks.',
            'Flowchart' : 'is a diagram showing the steps in a program.',
            'Concatenation' : 'is to combine strings using the plus sign.'}

# loop for printing the key-value pairs from the dictionary
for word, definition in glossary.items():
    print(f"{word.title()}: {definition}\n")