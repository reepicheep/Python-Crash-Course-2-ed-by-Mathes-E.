# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
# You’ll have to think of someone else to invite.
# a) Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# b) Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# c) Print a second set of invitation messages, one for each person who is still in your list.

guest_list = ["Peter", "Lucy", "Reepicheep"]

print(f"{guest_list[-2]} cannot make it")

guest_list[-2] = "Mary"

invite_peter = f"Dear {guest_list[0]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_mary = f"Dear {guest_list[1]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_reepicheep = f"Dear {guest_list[-1]}, I would like to invite you to dinner on Saturday at 8 pm."

print(invite_peter)
print(invite_mary)
print(invite_reepicheep)