"""
Python’s iterators and iterables are two different but related tools that come
in handy when you need to iterate over a data stream or container.


Two way to iterate over any kind of code:
Repeating the target code as many times as you need in a sequence
Putting the target code in a loop that runs as many times as you need


When you use a while or for loop to repeat a piece of code several times,
you’re actually running an iteration.
That’s the name given to the process itself.

In Python, if your iteration process requires going through the values or items
in a data collection one item at a time, then you’ll need another piece to
complete the puzzle. You’ll need an iterator.
"""

"""
What Is an Iterator in Python?
In Python, an iterator is an object that allows you to iterate over collections
of data, such as lists, tuples, dictionaries, and sets.

Python iterators implement the iterator design pattern, which allows you to
traverse a container and access its elements. The iterator pattern decouples
the iteration algorithms from container data structures.
"""
"""
Iterators take responsibility for two main actions:

Returning the data from a stream or container one item at a time
Keeping track of the current and visited items

In summary, an iterator will yield each item or value from a collection or a
stream of data while doing all the internal bookkeeping required to maintain
the state of the iteration process.
"""
"""
Python iterators must implement a well-established internal structure known as
the iterator protocol.
"""

"""
The .__iter__() method of an iterator typically returns self, which holds a
reference to the current object: the iterator itself.

The .__next__() method will be a bit more complex depending on what you’re
trying to do with your iterator.
"""


def __iter__(self):
    return self


"""
The only responsibility of .__iter__() is to return an iterator object.
So, this method will typically just return self, which holds the current
instance.
"""
"""
This method must return the next item from the data stream. It should also
raise a StopIteration exception when no more items are available in the data
stream.
 """
"""
When to use Iterator?

The most generic use case of a Python iterator is to allow iteration over a
stream of data or a container data structure.
data can come from different sources, such as your local disk, a database, and
a network.
In these situations, iterators allow you to process the datasets one item at a
time without exhausting the memory resources of your system, which is one of
the most attractive features of iterators.
"""

"""
Creating Different Types of Iterators.

Take a stream of data and yield data items as they appear in the original data

Take a data stream, transform each item, and yield transformed items

Take no input data, generating new data as a result of some computation to
finally yield the generated items
"""

"""
Yielding the Original Data
"""


class SquenceItertor:

    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self._index < len(self._sequence)):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration


"""
You can create an iterator that doesn’t define an .__iter__() method, in which
case its .__next__() method will still work. However, you must implement
.__iter__() if you want your iterator to work in for loops.
This loop always calls .__iter__() to initialize the iterator.
"""

for item in SquenceItertor([1, 2, 3, 4]):
    print(item)

"""
how Python’s for loops work internally.
The following code simulates the complete process:
"""

sequence = SquenceItertor([1, 2, 3, 4])

iterator = sequence.__iter__()
while True:
    try:
        item = iterator.__next__()
    except StopIteration:
        break
    else:
        print(item)


"""
You shouldn’t use .__iter__() and .__next__() directly in your code. Instead,
you should use the built-in iter() and next() functions, which fall back to
calling the corresponding special methods.
"""
"""
Transforming the Input Data
Say that you want to write an iterator that takes a sequence of numbers,
computes the square value of each number, and yields those values on demand.
"""


class SquareIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            square = self._sequence[self._index] ** 2
            self._index += 1
            return square
        else:
            raise StopIteration


"""
The first part of this SquareIterator class is the same as your
SequenceIterator class. The .__next__() method is also pretty similar.
The only difference is that before returning the current item,
the method computes its square value. This computation performs a
transformation on each data point.
"""

for square in SquareIterator([2, 4, 6, 8]):
    print(square)

"""
Generating New Data
You can also create custom iterators that generate a stream of new data from a
given computation without taking a data stream as input.
"""


class FibonacciIterator:
    def __init__(self, stop=10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next,
            )
            return fib_number
        else:
            raise StopIteration


"""
You start this method with a conditional that checks if the current sequence
index hasn’t reached the ._stop value, in which case you increment the
current index to control the iteration process. Then you compute the
Fibonacci number that corresponds to the current index, returning
the result to the caller of .__next__().
"""
for fib in FibonacciIterator():
    print(fib)
