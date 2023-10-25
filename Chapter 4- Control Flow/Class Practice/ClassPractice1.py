# Making a code that shows: For every assignment done, the user gets 2 chocolates.

assignment = int(input("How many assignments did you do today? - "))
chocolate = 0

# condition will be: for every 1 assignment done is 2 chocolates.
if assignment >= 1 :
    chocolate = assignment * 2
else:
    chocolate = 0

# display how many assignments User has done and how many chocolates they gain for that.
if assignment <= 1:
    print(f"For doing {assignment} assignment, you gain {chocolate} chocolates today!")
else:
    print(f"For doing {assignment} assignments, you gain {chocolate} chocolates today!")

if assignment == 0:
    print(f"You know what that means. Go do something productive right now.")