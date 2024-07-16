#  sets in python

# 1. Create a set

# s = {}
# This is a dictionary, not a set. To create a set, use the set() function.

# s = {1}
# this is a set

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# # intersection
print(set2 & set1)
# print(set2.intersection(set1)) or print(set1.intersection(set2))

# union
print(set2 | set1)
# print(set2.union(set1)) or print(set1.union(set2))

# difference
print(set2 - set1) or print(set1 - set2)
# print(set2.difference(set1)) or print(set1.difference(set2))

# symmetric difference

print(set2 ^ set1)
# print(set2.symmetric_difference(set1)) or print(set1.symmetric_difference(set2))







