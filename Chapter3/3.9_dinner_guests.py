# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.

# 3.4_guest_list.py

guest_list = ["Peter", "Lucy", "Reepicheep"]

"""
invite_peter = f"Dear {guest_list[0]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_lucy = f"Dear {guest_list[1]}, I would like to invite you to dinner on Saturday at 8 pm."
invite_reepicheep = f"Dear {guest_list[-1]}, I would like to invite you to dinner on Saturday at 8 pm."

print(invite_peter)
print(invite_lucy)
print(invite_reepicheep)
"""

guest_list_length = len(guest_list)
print(f"I am inviting {guest_list_length} people to dinner.")
