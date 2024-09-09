
from collections.abc import Iterator
"""
Inheriting From collections.abc.Iterator
The collections.abc module includes an abstract base class (ABC) called
Iterator.bYou can use this ABC to create your custom iterators quickly.
This class provides basic implementations for the .__iter__() method.
"""
"""
It also provides a .__subclasshook__() class method that ensures only
classes implementing the iterator protocol will be considered subclasses of
Iterator.
"""


class SequenceIterator(Iterator):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


for seq in SequenceIterator([1, 3, 5, 10]):
    print(seq)


"""
Creating Generator Iterators
"""

"""
To create a generator function, you must use the yield keyword to yield
the values one by one.

Here’s how you can write a generator function that returns an iterator that’s
equivalent to your SequenceIterator class

"""


def sequence_generator(sequence):
    for item in sequence:
        yield item


sequence_generator([1, 2, 3, 4])

for number in sequence_generator([1, 2, 3, 4]):
    print(number)


"""
You can use this iterator in a for loop as you would use a class-based iterator
Internally, the iterator will run the original loop, yielding items on demand
until the loop consumes the input sequence, in which case the iterator will
automatically raise a StopIteration exception.
"""

"""
Generator functions are a great tool for creating function-based iterators that
save you a lot of work. You just have to write a function, which will often be
less complex than a class-based iterator. If you compare sequence_generator()
with its equivalent class-based iterator, SequenceIterator, then you’ll note a
big difference between them. The function-based iterator is way simpler and
more straightforward to write and understand.
"""

"""
Using Generator Expressions to Create Iterators
If you like generator functions, then you’ll love generator expressions.
These are particular types of expressions that return generator iterators.
The syntax of a generator expression is almost the same as that of a list
comprehension. You only need to turn the square brackets ([]) into parentheses:
"""

var = [item for item in [1, 2, 3, 4]]  # List comprehension


var = (item for item in [1, 2, 3, 4])  # Generator expression


generator_expression = (item for item in [1, 2, 3, 4])
for item in generator_expression:
    print(item)

"""
Iterators and generators are pretty memory-efficient when you compare them with
regular functions, container data types, and comprehensions. With iterators and
generators, you don’t need to store all the data in your compter’s memory at
the same time.

Iterators and generators also allow you to completely decouple iteration from
processing individual items. They let you connect multiple data processing
stages to create memory-efficient data processing pipelines.
"""

"""
Returning Iterators Instead of Container Types
"""


