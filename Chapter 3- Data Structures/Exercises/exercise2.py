"""Exercise 2: Greetings 
Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them. 
The text of each message should be the same, but each message should be personalized with the person’s name."""

## same list from the previous exercise
names=["Angelica", "Rennzo", "Eric", "Temilade", "Seb"]
# displaying the same message but with different names using f-string and list slicing
print(f'One of the reasons I am still here today is you, {names[0]}.')
print(f'One of the reasons I am still here today is you, {names[1]}.')
print(f'One of the reasons I am still here today is you, {names[-3]}.')
print(f'One of the reasons I am still here today is you, {names[3]}.')
print(f'One of the reasons I am still here today is you, {names[-1]}.')
