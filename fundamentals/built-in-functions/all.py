"""
all(iterable)
Return True if all elements of the iterable are true
(or if the iterable is empty)
"""
# all values are True
list1 = [1, 2, 3, 4]
print(all(list1))

# one value is False
list2 = [0, 2, 4]
print(all(list2))

# all values are False
list3 = [0, False]
print(all(list3))

# empty list
list4 = []
print(all(list4))
