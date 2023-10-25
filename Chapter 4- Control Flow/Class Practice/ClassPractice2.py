# Nested Decision Structure

# Making a code about whether User may or may not join the Town's Sports Club.

# state that the following questions will be answered by yes or no--Yes represented by 1 and No represented by 0.
print('The following are Yes and No questions. Please enter "1" for "Yes" and "0" for "No".\n')

health = int(input("Are you currently experiencing a health condition such as asthma or bone problems? - "))
clubs = int(input("Have you ever experienced being in any sports club in your school, community, or any of the like? - "))

if health == 0:
    if clubs == 1:
        print("Congratulations! You may join the Town Sports Club.")
    else:
        print("Sorry, you may not join the town sports club. Try again once you experienced joining in at least one club in your school or any other communities.")
else:
    print("Sorry, but due to your health condition, you may not join the Town's Sports Club.")