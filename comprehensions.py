# list comprehensions
# [expr for val in collection]

# list comprehensions
t = tuple(i for i in range(10)) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# list comprehensions with condition
t = tuple(i ** 2 for i in range(10) if i % 2 == 0) # (0, 4, 16, 36, 64)