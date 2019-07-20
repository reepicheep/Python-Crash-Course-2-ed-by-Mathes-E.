# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# a) Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
# b) Use insert() to add one new guest to the beginning of your list.
# c) Use insert() to add one new guest to the middle of your list.
# d) Use append() to add one new guest to the end of your list.
# e) Print a new set of invitation messages, one for each person in your list


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

# print(more_guests)

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