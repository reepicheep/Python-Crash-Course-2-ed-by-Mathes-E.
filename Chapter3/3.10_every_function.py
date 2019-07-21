"""
3-10. Every Function: Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
"""

# CHANGING, ADDING, AND REMOVING ELEMENTS

languages = ["English", "Bulgarian", "Russian", "French", "Portugese"]
print(languages)

# Modifying Elements in a List

languages[0] = "German"
print(languages)

# Adding Elements to a List

# Appending Elements to the End of a List The

languages.append('English')
print(languages)

# Inserting Elements into a List You

languages.insert(0, "Polish")
print(languages)

# Removing Elements from a List

# Removing an Item Using the del Statement

del languages[0]
print(languages)
# You can no longer access the value that was removed from the list after the del statement is used

# Removing an Item Using the pop() Method
# The pop() method removes the last item in a list, but it lets you work with that item after removing it.

popped_languages = languages.pop()
print(languages)
print(popped_languages)

# Popping Items from any Position in a List

first_learnt = languages.pop(0)
print(languages)
# When you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

# Removing an Item by Value

languages.remove('French')
print(languages)
# The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to make sure all occurrences of the value are removed.

# ORGANIZING A LIST

# Sorting a List Permanently with the sort() Method

languages.sort()
print(languages)

# in reverse ALPHABETICAL order
languages.sort(reverse=True)
print(languages)


# Sorting a List Temporarily with the sorted() Function

print(languages)

print(sorted(languages))

print(languages)

    # Accepting a reverse=True argument if you want to display a list in reverse ALPHABETICAL order

print(sorted(languages, reverse=True))

    # Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital letters when determining a sort order, and specifying the exact order can be more complex than we want to deal with at this time.

# Printing a List in Reverse Order, reverse(), Permanently Reversing

print(languages)

languages.reverse()
print(languages)

    # Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list.

    # The reverse() method changes the order of a list permanently, but you canrevert to the original order anytime by applying reverse() to the same list a second time.

languages.reverse()
print(languages)

# Finding the Length of a List

print(len(languages))

    # Python counts the items in a list starting with one, so you shouldn’t run into any off-by-one errors when determining the length of a list.