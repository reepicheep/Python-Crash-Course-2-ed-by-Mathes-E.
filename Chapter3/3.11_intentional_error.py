# 3-11. Intentional Error: If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

languages = ["English", "Bulgarian", "Russian", "French", "Portugese"]

"""
# Index Error - IndexError: list index out of range
# Because of the off-by-one nature of indexing in lists, this error is typical. 
print(languages[5])
"""

# Correction
print(languages[-1])