"""Exercise 5: Change Guest List 
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still in your list."""

invite=["Grandpa Roger", "Ate Daylin", "Grandma Priscila", "Papa Willie"]

# invitations
print(f"Invitation to {invite[0]}")
print(f"""  Dearest {invite[0]},
      
        I know we didn't get to spend a lot of time together with you when you were still here, 
        but still, I would love to have dinner with you sometime.
      
    With lots of love,
    Precy <3\n\n""")

print(f"Invitation to {invite[1]}")
print(f"""  Dearest {invite[1]},
      
        It's been so long since we last saw each other. I believe I'm growing up well, so I hope you're also doing fine in life.
        I would love to have dinner with you and do a lot of catching up.
      
    With lots of love,
    Precy <3\n\n""")

print(f"Invitation to {invite[-2]}")
print(f"""  Dearest {invite[-2]},
      
        It's been a few years since I haven't gone back to the Philippines and you know there isn't a day when I'm not missing you all.
        I would love to have dinner with you when I come back there.
      
    With lots of love,
    Precy <3\n\n""")

print(f"Invitation to {invite[-1]}")
print(f"""  Dearest {invite[-1]},
      
        It's been a few years since I haven't gone back to the Philippines and you know there isn't a day when I'm not missing you all.
        I would love to have dinner with you when I come back there.

    With lots of love,
    Precy <3\n\n""")
# ~~~ end of exercise 3-4 program ~~~

# stating the guest who can't make it
print(f"My guest who won't be able to make it to dinner is: {invite[1]}\n")

invite[1]="Aunt Mika" # replaces the name of the guest who can't make it

# invitations
print(f"Invitation to {invite[0]}")
print(f"""  Dearest {invite[0]},
      
        I know we didn't get to spend a lot of time together with you when you were still here, 
        but still, I would love to have dinner with you sometime.
      
    With lots of love,
    Precy <3\n\n""")

# content of the message was also changed as the guest had been changed
print(f"Invitation to {invite[1]}")
print(f"""  Dearest {invite[1]},
      
        It's been a few years since I haven't gone back to the Philippines and you know there isn't a day when I'm not missing you all.
        I would love to have dinner with you when I come back there.
      
    With lots of love,
    Precy <3\n\n""")

print(f"Invitation to {invite[-2]}")
print(f"""  Dearest {invite[-2]},
      
        It's been a few years since I haven't gone back to the Philippines and you know there isn't a day when I'm not missing you all.
        I would love to have dinner with you when I come back there.
      
    With lots of love,
    Precy <3\n\n""")

print(f"Invitation to {invite[-1]}")
print(f"""  Dearest {invite[-1]},
      
        It's been a few years since I haven't gone back to the Philippines and you know there isn't a day when I'm not missing you all.
        I would love to have dinner with you when I come back there.

    With lots of love,
    Precy <3\n\n""")
