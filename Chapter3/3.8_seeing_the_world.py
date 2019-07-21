"""
3-8. Seeing the World: Think of at least five places in the world you’d like to visit.

a) Store the locations in a list. Make sure the list is not in alphabetical order.

b) Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.

c) Use sorted() to print your list in alphabetical order without modifying the actual list.

d) Show that your list is still in its original order by printing it.

e) Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.

f) Show that your list is still in its original order by printing it again.

g) Use reverse() to change the order of your list. Print the list to show that its order has changed.

h) Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.

i) Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.

j) Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.

"""
# a)
visit_places = ["Canberra", "Las Vegas", "Boston", "Paris", "Monaco"]

# b)
print(visit_places)

# c)
print(sorted(visit_places))

# d)
print(visit_places)

# e)
"""
reverse_sorted = sorted(visit_places, reverse=True)
print(reverse_sorted)
"""
print(sorted(visit_places, reverse=True))

# f)
print(visit_places)

# g)
visit_places.reverse()
print(visit_places)

# h)
visit_places.reverse()
print(visit_places)

# i)
visit_places.sort()
print(visit_places)

# j)
visit_places.sort(reverse=True)
print(visit_places)
