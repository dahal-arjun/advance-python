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


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, major):
        super().__init__(name=name)
        self.major = major


john = Student("John", "Computer Science")
print(type(john))

"""
When you create an object python assigns the unique id for the object
the id is read-only. The type of object is generally fixed but it can be
reassigned. It is not read-only. You can reassign by calling .__class__
attribute to different class
"""

john.__class__ = Person

print(type(john))
print(john.name)
print(john.major)

"""
What just happened? you could access the major even though the class doesn't
have that attribute.
The change modifies the object's type not the object's current attributes.
What does that means?
In python type is also reassignable only thing that is read-only is id, the
type we reassigned changed into different type.
An object’s value is probably the only characteristic that you should change.
The changes that you can perform on a mutable object’s
value are known as mutations.
"""

"""
Built in immutable types:
    single-item data type:
        integer, floats, complex numbers and boolean
    container types:
        string, tuples
"""


"""
when you modify the item inside the collection, list or dictionery
you are not modifying the id or creating the dublicate you are
just changing the value/content of that object. By the defination
the mutable object's id is unchanged and other things are changable
i.e internal state, value, and others.

"""

"""
When and What makes difference while working with mutable and immutable values?
Immutable values:
    If you use immutable objects, It will take more meomory, why?
    By defination you cannot change aything of an immutable data, you need to
    copy value and modify as per need meaning same data will be dublicated
    in the memory.

Mutable values:
    If you work with mutable values let's suppose you want to change something
    inside the mutable value, In python everything has a refrence to memory,
    and in mutable data type it doesn't change the id,
    if i change value anywhere the updated value will be taken,
    which will just introduce the bugs everywhere.
    This was when you have only 1 thread accessing the value/resource
    Now assume working with multiple threads and you are modifying with
    multiple threads, this will basically introduce alot of bug and headachae.
    TODO: explore the multi thread programms, parallel processing in python and
    multi-processing etc.
"""

"""
Exaples for Built in data types in Python.
Right now the ways I know to check the immutable or mutable value,
is to look  the idand is oprator.
"""

# Numbers
number = 123
print(id(number))

number_add_1 = number+1
print(id(number_add_1))

"""
Here we are getting totally different values if we check id,
the value we have modified was copied and then addded 1
"""

"""
More examples on immutable values
"""
new_number = number
print(id(number))
print(id(new_number))

"""
Here we are getting same id? but why?
we are using immutable data type, python loves to point to the memory
by default, we are not modifying or doing anything, when we modify any value
it will keep the value original and the new opration will be perofmed
in new variable pointing to different location.
"""

"""
How boolean works now? the boolean is basically a constant which is set
to 0 and 1. The bool is the subclass of int.
"""

print(issubclass(bool, int))
print(isinstance(True, int))
print(int(True))

"""
Here we have used two built in methods, i.e. issubclass and isinstance...
These will check if the object is subclass of parent class,
and other checks the intance of an class,
int() is just parsing the data to int.
TODO: how parsing works? inside the python.
TODO research on: how issubclass and isinstance works? How it matches and knows
which is the subclass?
"""

"""
String: strings are the squence of individual characters, they are sequences
you can access using indexing operator i.e. [].
and inside that bracket index.
"""
greetings = "abcd"
print(greetings[1])


print(id(greetings[2]))
print(id(greetings[1]))
print(id(greetings[0]))
"""
the each individual data types inside string has an unique id which cannot be
reassigned. This means string should be mutable but it is not.
TODO: Find the algorithm which is making the string immutable.
"""

# greetings[2] = "A"

"""
You can use a bytearray object to emulate a mutable string,
which will help you deal with those memory and performance issues:
"""
mutable_greeting = bytearray(greetings.encode("utf-8"))
print(id(mutable_greeting))
mutable_greeting[1] = ord("E")
print(mutable_greeting)
print(id(mutable_greeting))

"""
If you do any operations of string it will destroy and create new copy with the
changes.
"""

"""
Bytes:
    The built in bytes type is also immutable type in python.
    Byte literals may look pretty similar to string literals because their
    syntax is mostly the same as that of string literals.
    You just need to add a b prefix:
"""
greeting_bytes = b"Hello, World!"
print(type(greeting_bytes))

"""
A significant difference between strings and bytes is that
the latter only allows for ASCII characters in its literals.
If you ever need to store a binary value over 127 in a bytes object,
then you must enter it using the appropriate escape sequence.
Alternatively, you can turn a Python string into a bytes object
using a specific character encoding and the .encode() method:
"""
print(bytes("Español".encode("utf-8")))


"""
Tupels:
    Python’s tuples are another example of an immutable collection of data.
    You can’t modify them once created. Like strings, tuples are sequences.
    However, unlike strings,
    tuples allow you to store any type of object rather than just characters.
"""
letters = ("a", "b", "c", "d")
print(type(letters))

letters = "a", "b", "c", "d"
print(type(letters))
# You can assess items just like the string.
print(letters[0])
# You cannot reassign
# letters[0] = "A"


"""
Mutable Data Types:
    Mutable data types are another face of the built-in types in Python.
    The language provides a few useful mutable collection types
    that you can use in many situations.
    These types allow you to change the value of specific items
    without affecting the identity of the container object.
"""

"""
Lists:
    lists are sequences of arbitrary objects.
    you can change the value of a list object in place.
    You can change the value of any item without altering the list’s identity
"""

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[0])
print(digits[3:7])
print(digits[2::2])
print(digits[2::2])

