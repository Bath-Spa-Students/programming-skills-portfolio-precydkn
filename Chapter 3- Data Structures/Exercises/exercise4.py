"""Exercise 4: Guest List 
If you could invite anyone, living or deceased, to dinner, who would you invite? 
Make a list that includes at least three people you’d like to invite to dinner. 
Then use your list to print a message to each person, inviting them to dinner."""

# list of people to invite
invite=["Grandpa Roger", "Ate Daylin", "Grandma Priscila", "Papa Willie"]

## invitations with personalized messages per person
# for first invitee
print(f"Invitation to {invite[0]}") # displays the name of the first invitee using f-string and list slicing
print(f"""  Dearest {invite[0]},
      
        I know we didn't get to spend a lot of time together with you when you were still here, 
        but still, I would love to have dinner with you sometime.
      
    With lots of love,
    Precy <3\n\n""") # displays the invitation

# for second invitee
print(f"Invitation to {invite[1]}")  # displays the name of the second invitee using f-string and list slicing
print(f"""  Dearest {invite[1]},
      
        It's been so long since we last saw each other. I believe I'm growing up well, so I hope you're also doing fine in life.
        I would love to have dinner with you and do a lot of catching up.
      
    With lots of love,
    Precy <3\n\n""") # displays the invitation

# for third invitee
print(f"Invitation to {invite[-2]}")  # displays the name of the third invitee using f-string and list slicing
print(f"""  Dearest {invite[-2]},
      
        It's been a few years since I haven't gone back to the Philippines and you know there isn't a day when I'm not missing you all.
        I would love to have dinner with you when I come back there.
      
    With lots of love,
    Precy <3\n\n""") # displays the invitation

# for last invitee
print(f"Invitation to {invite[-1]}")  # displays the name of the last invitee using f-string and list slicing
print(f"""  Dearest {invite[-1]},
      
        It's been a few years since I haven't gone back to the Philippines and you know there isn't a day when I'm not missing you all.
        I would love to have dinner with you when I come back there.

    With lots of love,
    Precy <3\n\n""") # displays the invitation
