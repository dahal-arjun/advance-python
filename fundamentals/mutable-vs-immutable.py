"""
Link-for-mutable-vs -immutable-in-python
- https://ioflood.com/blog/mutable-vs-immutable-in-python-object-data-types-explained
- https://realpython.com/python-mutable-vs-immutable-types/
- https://www.linkedin.com/pulse/understanding-mutable-immutable-data-types-python-rasmi-ranjan-swain/
- https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python

Link-for-copy.py
- https://docs.python.org/3/library/copy.html#
I Will be adding summary but always feel free to go and check out the original
resource by yourself.
"""

"""
What is variable and how creating a variable works?
    - Variables are the lables attached to the objects in memory.
    - Varibles just points the position where the concrete object live.
    - When we define a variable using = ("assignment statement").
        We are saying that please point to the object, defined after the =
        please lable that location of the object as name it as variable name
        for e.g: example = "the value is example and this is an object of string"
        here, we are saying the object id or refrence id which is the location of memory
        assign it to example. So, whenever we call it go to the location
        and return the value from the memory.
        TODO: understand how refrencing works and how variables are created?
              lifecycle of creating variable, adding the refrence, and how
              python tracks the object?


What is object and how does this works?
    - Objects and variables are not same but they are closely related to each other
    - Object holds the information, they live inside memory.
    - When we create any object, of any class, we say take that amount of memory
        keep inside the memory and then when we want give us an unique id, so that
        we get the required data from memory.
    TODO: research on different ways of memory management done by python.

What after assigning the object to the varibale?(a="something")
    - Python will keep track of it (refrence of the object).
        If the object is mutable. You can mutate it's internal state,
        with the help of varibale name. Remember the variable name is like
        gate where it let's to access real value of the object, you are not
        modifying the varibale rather the object underneeth it.
        If the object is immutable, You cannot change anything you can just
        refrence it. You can read the value but not alter the value.

    - Garbage Collection
        If somehow your variable doesn't refrence any object then this will be
        collected and cleaned up by garbage collection. And then frees up the
        space so that other can use the memory.
        TODO: Study more about the garbage Collection, How python is using GC.

Characterstics of the Object, Value and Type.
    Everything in python is an object. numbers, strings, functions, classes
    and modules are all objects.
    Here are the core characterstics of python objects:
    - Value
        value is the pieces of data contained in object itself.
        num = 42
        isinstance(num, int)

    - Identity
       An object value lives in a memory. This specific address is known as the
       object's Identity. This identiy is an unique identifier which
       makes unique from other objects.
       An object’s identity is a read-only property,
       which means that you can’t change an object’s identity
       once the object has been created.
       to get the unique id you can use built in method id() from
       standard library.

    - Type
        The final characterstic of python is type.
        you can determine how the object is dereived from using built in method
        type()
        Even though .__class__ works, you should use type()
        to retrieve the type of a given object and
        avoid direct access to special attributes as much as possible,
        especially in cases where a dedicated built-in function exists.

What is Mutable and Immutable?
Mutable:
    - The ability to change its value after the object is created.
    - You can alter the internal data or attributes without creating new object
    - If you modify value of an mutable object, It will reflect in other places
      as well meaning the refrences will get the changed value.
      This behavior is known as aliasing.
Immutable:
    - The immutable values doesn't change after the creation of the object.
    - You cannot alter the internal data or attribute.
    - You have to destroy and then create new object
      You cannot modify the old object.

"""
# Example of object's value
num = 42
print(isinstance(num, int))
print(id(num))
print(type(num))
print(num.__class__())   # Another way to access the type of the variable
