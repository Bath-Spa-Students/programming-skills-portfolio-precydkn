'''A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. 
They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
You will to use the arithmetic operators to complete this exercise.'''

# assigning the values from the problem to variables
budget = 50
usbPrice = 6
numOfUsb = int(budget/usbPrice) # formula to know how many usbs can be bought with the money
totalPrice = usbPrice*numOfUsb # formula to know the total price of the usbs
moneyLeft = budget-totalPrice # formula to know the change left for the girl after buying

# displaying the answers to the problem
print(f'''The number of USB sticks that the girl can buy for £50 is {numOfUsb}.\nThe total price of the {numOfUsb} USB sticks is {totalPrice}, leaving her with £{moneyLeft}.''')
