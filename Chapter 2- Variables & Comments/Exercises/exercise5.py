'''A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. 
They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
You will to use the arithmetic operators to complete this exercise.'''

budget = 50
usbPrice = 6
numOfUsb = int(budget/usbPrice)
totalPrice = usbPrice*numOfUsb
moneyLeft = budget-totalPrice

print(f'''The number of USB sticks that the girl can buy for £50 is {numOfUsb}.\nThe total price of the {numOfUsb} USB sticks is {totalPrice}, leaving her with £{moneyLeft}.''')