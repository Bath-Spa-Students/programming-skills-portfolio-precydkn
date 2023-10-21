"""Exercise 6: Shrinking Guest List 
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, 
print a message to that person letting them know you’re sorry you can’t invite them to dinner.
•	 Print a message to each of the two people still on your list, letting them know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list 
at the end of your program."""

invite=["Grandpa Roger", "Ate Daylin", "Grandma Priscila", "Papa Willie"]
# state the guest who can't make it
print(f"My guest who won't be able to make it to diner is: {invite[1]}\n")

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
# ~~~ end of exercise 3-5 program ~~~

print("Unfortunately, I can only invite two guests because of the limited tables in the venue.\n")

# removing "Grandpa Roger"
invite.pop(0)
# uninvitation message to him
print("Message of uninvitation to Grandpa Roger")
print(f"""  Dearest Grandpa Roger,
      
        I know I recently invited you for dinner, but sadly, I only have space for two guests at the moment.
        I guess we'll just have to postpone this for another time. Hope to have you next time then, gramps.
      
    Sincerely,
    Precy <3\n\n""")

# removing "Papa Willie"
invite.pop(-1)
# uninvitation message to him
print("Message of uninvitation to Papa Willie")
print(f"""  Dearest Papa Willie,
      
        I know I recently invited you for dinner, but sadly, I only have space for two guests at the moment.
        I guess we'll just have to postpone this for another time. Hope to have you next time then, pops.
      
    Sincerely,
    Precy <3\n\n""")

# still invited messages
print(f"Invitation to {invite[0]}")
print(f"""  Dearest {invite[0]},
      
        If you heard about my situation of only being able to have two guests for dinner this time, worry not, 
        as you are still one of the two people I'm inviting. That said, I hope to see you there then.
      
    Sincerely,
    Precy <3\n\n""")

print(f"Invitation to {invite[1]}")
print(f"""  Dearest {invite[1]},
      
        If you heard about my situation of only being able to have two guests for dinner this time, worry not, 
        as you are still one of the two people I'm inviting. That said, I hope to see you there then.
      
    Sincerely,
    Precy <3\n\n""")

# emptying invitation list
print(invite)
del(invite[-1])
del(invite[0])
print(invite)