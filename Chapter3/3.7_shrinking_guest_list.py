# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# a) Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# b) Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# c) Print a message to each of the two people still on your list, letting them know they’re still invited.
# d) Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

guest_list = ["Peter", "Lucy", "Reepicheep"]

# print(f"{guest_list[-2]} cannot make it")

guest_list[-2] = "Mary"

invite_peter = f"Dear {guest_list[0]}, My invitation to dinner on Saturday at 8 pm still stays. However I have found a bigger dinner table and more people will possibly be coming."
invite_mary = f"Dear {guest_list[1]}, My invitation to dinner on Saturday at 8 pm still stays. However I have found a bigger dinner table and more people will possibly be coming."
invite_reepicheep = f"Dear {guest_list[-1]}, My invitation to dinner on Saturday at 8 pm still stays. However I have found a bigger dinner table and more people will possibly be coming."

print(invite_peter)
print(invite_mary)
print(invite_reepicheep)

more_guests = guest_list

more_guests.insert(0, "John")
more_guests.insert(2, "George")
more_guests.append("Nicolas")

print(more_guests)


invite_john = f"Dear {guest_list[0]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_peter = f"Dear {guest_list[1]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_george = f"Dear {guest_list[2]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_mary = f"Dear {guest_list[3]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_reepicheep = f"Dear {guest_list[-2]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_nocolas = f"Dear {guest_list[-1]}, I would like to invite you to dinner on Saturday at 8 pm."

print(invite_john)
print(invite_peter)
print(invite_george)
print(invite_mary)
print(invite_reepicheep)
print(invite_nocolas)

# a)

invite_change_john = f"Dear {guest_list[0]}, unfortunately my new dinner table won’t arrive in time for the dinner, and I have space for only two guests for my dinner on Saturday at 8 pm. Please wait for additional invite."
invite_change_peter = f"Dear {guest_list[1]}, unfortunately my new dinner table won’t arrive in time for the dinner, and I have space for only two guests for my dinner on Saturday at 8 pm. Please wait for additional invite."
invite_change_george = f"Dear {guest_list[2]}, unfortunately my new dinner table won’t arrive in time for the dinner, and I have space for only two guests for my dinner on Saturday at 8 pm. Please wait for additional invite."
invite_change_mary = f"Dear {guest_list[3]}, unfortunately my new dinner table won’t arrive in time for the dinner, and I have space for only two guests for my dinner on Saturday at 8 pm. Please wait for additional invite."
invite_change_reepicheep = f"Dear {guest_list[-2]}, unfortunately my new dinner table won’t arrive in time for the dinner, and I have space for only two guests for my dinner on Saturday at 8 pm. Please wait for additional invite."
invite_change_nocolas = f"Dear {guest_list[-1]}, unfortunately my new dinner table won’t arrive in time for the dinner, and I have space for only two guests for my dinner on Saturday at 8 pm. Please wait for additional invite."

print(invite_change_john)
print(invite_change_peter)
print(invite_change_george)
print(invite_change_mary)
print(invite_change_reepicheep)
print(invite_change_nocolas)


# b)

remove_nicolas = more_guests.pop()
print(more_guests)
print(f"Dear {remove_nicolas}, I am sorry but I have had to reduce the number of my guests and will avail of the honor of inviting you again at a later date. Thank you!")


remove_reepicheep = "Reepicheep"
more_guests.remove("Reepicheep")
print(more_guests)
print(f"Dear {remove_reepicheep}, I am sorry but I have had to reduce the number of my guests and will avail of the honor of inviting you again at a later date. Thank you!")

remove_mary = more_guests.pop(-1)
print(more_guests)
print(f"Dear {remove_mary}, I am sorry but I have had to reduce the number of my guests and will avail of the honor of inviting you again at a later date. Thank you!")

remove_george = more_guests.pop(-1)
print(more_guests)
print(f"Dear {remove_george}, I am sorry but I have had to reduce the number of my guests and will avail of the honor of inviting you again at a later date. Thank you!")

# c)

print(f"Dear {more_guests[0]}, please feel still invited.")
print(f"Dear {more_guests[1]}, please feel still invited.")

# d)

del more_guests[0]
del more_guests[0]

print(more_guests)
