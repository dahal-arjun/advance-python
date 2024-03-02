"""

aiter(async_iterable)

source:
    https://docs.python.org/3/glossary.html#term-asynchronous-iterator
    https://docs.python.org/3/library/functions.html#aiter
    https://docs.python.org/3/glossary.html

New in version 3.10.
Return an asynchronous iterator for an asynchronous iterable.
Equivalent to calling x.__aiter__().

An object that implements the __aiter__() and __anext__() methods. __anext__()
must return an awaitable object. async for resolves the awaitables returned by
an asynchronous iterator’s __anext__() method until it raises a
StopAsyncIteration exception. Introduced by PEP 492.

An object, that can be used in an async for statement.
Must return an asynchronous iterator from its __aiter__() method.
Introduced by PEP 492.
I am skipping it till the iterable and iterator.
"""
