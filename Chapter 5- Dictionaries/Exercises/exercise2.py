## Exercise 2: Glossary
'''A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.'''

# gloassary of five words i learned in the previous chapters
glossary = {'Algorithm' : 'are sets of steps that are followed to perform a task.', 
            'Slicing' : 'getting a part or a section of values from a list.',
            'Index' : 'is the position of the elements in a list.',
            'Variable' : 'is where values are stored.',
            'Floats' : 'are positive and negative decimal numbers.'}

# print all the key-value written in the dictionary
print("Algorithm:", glossary['Algorithm'], "\n\nSlicing:", glossary['Slicing'],\
      "\n\nIndex:", glossary['Index'], "\n\nVariable:", glossary['Variable'], "\n\nFloats:", glossary['Floats'])