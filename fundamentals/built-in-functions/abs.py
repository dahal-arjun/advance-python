"""
Here we will learn different types of python's built in methods.
We will see from alphabetical order and do research on it.

Refrence:
    https://docs.python.org/3/library/functions.html
    https://www.toppr.com/guides/python-guide/references/methods-and-functions/python-abs/
"""

"""
abs()
It is used to return an absolute value of a number.
It supports int, float or other objects implementing
__abs__ dunder method.
If the argument is complex number it will return the magnitude.

In simple terms,
The absolute value of a number in any programming language is the value without
regard to its sign. It converts all numeric numbers to positive (or zero).

To remind you this is an built in method that means it doesn't need the import
statement.
"""

print(abs(-10))
print(abs(10))
print(abs(10.10))
print(abs(-10.10))

complex1 = (10 + 5j)
print(abs(complex1))

complex2 = (-8 + 4j)
print(abs(complex2))

complex3 = (2 - 7j)
print(abs(complex3))

complex4 = (-15 - 3j)
print(abs(complex4))

num_list = [-43, -5.76, 6+2j, -283]
mappedlist = map(abs, num_list)
print(list(mappedlist))
