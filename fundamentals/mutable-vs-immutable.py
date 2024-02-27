import copy


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
print(id(digits))
print(digits[0])
print(digits[3:7])
print(digits[2::2])
print(digits[2::2])
digits[1] = 2  # mutation
print(id(digits))

numbers = [1, 2, 314]
print(id(numbers))
print(id(numbers[2]))
numbers[2] = 3  # mutation
print(id(numbers[2]))
print(numbers)

"""
After this operation, you’ve lost all the references to your old 314 value.
Because of this, Python garbage-collects the old 314 and
frees the corresponding memory.
"""
letters = ["A", "B", "c", "d"]
letters[2:] = ["C", "D"]
print(letters)
"""
In this example, you mutate your letters list by replacing the letters
from index 2 up to the end of the list with uppercase letters.
"""

# Regular operator
letters = ["A", "B", "C"] * 3
letters


# Augmented operator
letters = ["A", "B", "C"]
print(id(letters))

letters *= 3
print(letters)

print(id(letters))


"""
Both mutable and immutable sequences support the += and *= augmented assignment
operators, but they do so differently. Mutable sequences like lists support the
+= operator through the .__iadd__() method, which performs an
in-place addition.

Similarly, mutable sequences support the *= operator through the .__imul__()
method, which also performs the operation in place, modifying the underlying
sequence.

In contrast, immutable sequences, such as tuples and strings, don’t have the
.__iadd__() and .__imul__() methods. Instead, augmented concatenations and
repetitions fall back to calling  .__add__() and .__mul__(), respectively.
These two methods don’t modify the underlying sequence in place
but return new sequences.

"""

"""
Dictionary:
    The keys of a dictionary work as unique identifiers that hold references to
    specific values. In other words, keys are like variables defined within a
    dictionary. You can use keys to access and mutate the values stored in a
    given dictionary.
"""
inventory = {"apple": 100, "orange": 80, "banana": 120}
print(inventory)
inventory["orange"] = 140  # Change
print(inventory)
inventory["lemon"] = 200  # Add
print(inventory)
del inventory["banana"]  # Remove
print(inventory)
# this should throw error KeyError as key is not found del inventory["grape"]
print(inventory)


"""
: Unfortunately, Python doesn’t have a built-in immutable dictionary-like type.
This type would be beneficial in situations where you need to cache function
calls that take dictionaries as arguments.
Caching requires the arguments to be hashable,
A quick solution to this caching issue would be to transform the dictionaries
into tuples of key-value pairs with the .items() method.

the keys in a dictionary must be unique. You can’t have duplicate keys.
Keys also have another important constraint. They must be hashable objects.

For an object to be hashable, you must be able to pass it to a hash function
and get a unique hash code. To achieve this, your object must be unchangeable.
In other words, the object’s value must never change during its lifetime.

According to this definition, immutable types, such as numbers, Booleans, and
strings, are hashable.
That means you can use them as dictionary keys.

There’s an important exception to this statement about immutable types.
Tuples are only hashable when all their items are also hashable.
Remember that tuples can store mutable objects,
in which case the underlying tuple won’t be hashable. You’ll learn more about
this specific behavior in the section Mutable Objects in Tuples.

In contrast, mutable types, such as lists, dictionaries, and sets,
can’t work as dictionary keys because they’re not hashable.
The reason? Their values can change during their lifetime.

Finally, dictionaries also support what’s called the union operator,
represented by the pipe symbol (|). This operator allows you to create
a new dictionary by merging key-value pairs from two existing dictionaries.

"""

inventory = {"apples": 42} | {"bananas": 24}
inventory


# Augmented operator
inventory = {"apples": 42}
print(id(inventory))

inventory |= {"bananas": 24}
print(inventory)

print(id(inventory))

"""
Sets:
    If you compare sets to lists, then you’ll find two main differences.
    First, sets don’t keep their data in any specific order, so you can’t use
    indices to access individual items.
    Second, sets don’t keep duplicate items, while lists do.
    Sets and dictionaries are closely related, though. In Python, a set works
    as a special dictionary that contains only keys instead of key-value pairs.
    Because of this characteristic, the items in a set must be hashable and
    unique.
"""
fruits = {"apple", "orange", "banana"}
fruits.add("lemon")
print(fruits)

fruits.add("orange")
print(fruits)


fruits.update({"grape", "orange"})
print(fruits)

"""
Python’s sets also implement operations from the original mathematical sets,
including union, intersection, difference, and symmetric difference.
All these operations return a new set object rather than modify the target
set in place.

Python sets also support some operators that allow you to perform
set operations on two existing sets.
"""

# Regular operators
{"apple", "orange"} | {"banana"}  # Union

{"apple", "orange"} & {"apple"}  # Intersection

{"apple", "orange"} - {"apple", "banana"}  # Difference

{"apple", "orange"} ^ {"apple", "banana"}  # Symmetric difference


# Augmented operators
fruits = {"apple", "orange"}
print(id(fruits))

fruits |= {"banana"}  # Augmented union
print(fruits)

print(id(fruits))


fruits = {"apple", "orange"}
print(id(fruits))

fruits &= {"apple"}  # Augmented intersection
print(fruits)

print(id(fruits))

"""
Opposite Variations of Sets and Bytes
Python also provides two lesser-known built-in types that provide variations
for the set and bytes types. For example, if you need an immutable set-like
data type, then you can take advantage of the built-in frozenset type.
Similarly, if you need a mutable bytes-like type, then you can use the
built-in bytearray type.
"""
fruits = frozenset(["apple", "orange", "banana"])
print(dir(fruits))

"""
Byte Arrays

This type has a mutable variant that’s called bytearray, which supports
in-place changes using indices. Like the bytes type, bytearray stores
binary data.

"""
greeting = bytearray(b"Hello, World!")
greeting[1] = ord("E")  # getting unicode value from E


"""
There are some extra considerations for you to keep in mind about some of the
types in this table:

Tuples can contain mutable types.
Booleans can only hold True or False.
Sets and frozen sets only accept unique, hashable items.
Dictionaries allow unique, hashable keys only.
"""

"""
Common Mutability-Related Gotchas

Aliasing Variables:
    Whenever you assign an existing variable to a new one, you create an alias
    for the original variable.
    Python variables don’t hold the data itself but references to the memory
    address where the data is stored. When you create an alias of an
    existing variable, both variables will hold the same reference.

    When you create aliases of variables pointing to immutable objects
    like numbers, strings, and tuples, you don’t have to worry about mutations.
    With mutable types, mutation on a given alias affects the rest of the
    aliases.
"""


"""
Mutatating Arguments in Functions

The variables inside the function is local.

When you create a variable inside a function by assigning global variable,
then it is just pointing at a varibale or just alising to the global variable
which basically means both of them are pointing to same memory location.

And when you modify the mutable value you are modifing the orignal value
in the memory. Let's see an example.
"""


def squares_of(numbers):
    for i, number in enumerate(numbers):
        numbers[i] = number ** 2
    return numbers


sample = [2, 3, 4]
print(squares_of(sample))

print(sample)


"""
Because you mutated the argument, these mutations affect the input data.
Now sample contains square values rather than the original data.
This may be the wrong final result because you’re losing your original data.
"""


def squares_of(numbers):
    result = []
    for number in numbers:
        result.append(number ** 2)
    return result


sample = [2, 3, 4]
print(squares_of(sample))

print(sample)

"""
If you pass an immutable object as an argument to a function,
then you can reassign that argument inside the function.
Changes won’t affect the original input object.
"""

counter = 0
print(id(counter))


def increment(value):
    value += 1
    print(id(value))
    return value


print(increment(counter))
print(increment(counter))
print(counter)
print(id(counter))

"""
 You can use Python’s global statement if you need the assignment to a global
 variable inside a function to affect the variable outside.
"""

counter = 0


def increment():
    global counter
    counter += 1


increment()
increment()

print(counter)


"""
Using Mutable Default Values
Optional arguments with default values are a great feature of Python functions
Default argument values allow you to write powerful, flexible functions.
A common recommendation in Python is to avoid mutable objects as default
argument values. Why?

Most Python developers will argue that using mutable types as default argument
values is a dangerous practice because the default value is defined when the
Python interpreter first parses the function. This means that if you call the
function multiple times while relying on the default value, then you’ll be
using the same object every time. The function becomes stateful.
It retains state between calls.
"""

"""
Because Python defines the default argument value when it first parses the
function and doesn’t overwrite it in every call, you’ll be working with the
same instance every time. Then, you don’t get the above output.
"""


def append_to(item, target=[]):
    target.append(item)
    return target


print(append_to(1))
print(append_to(2))
print(append_to(3))

"""
Wow! The list remembers the data between calls.
This happens because you’re relying on the same empty
list used as the default value of target.
This issue with mutable default argument values may be one of the reasons
why None is such a common default value in Python functions.

Even though using mutable default argument values is widely considered a
Python gotcha, you may find situations in which this rather weird behavior
may be useful.
"""

"""
Making Copies of Lists
Python’s lists are mutable. Because of this, it’s often useful to make a copy
of a given list before performing operations that would mutate the list
in place.You can copy a list in at least two ways. You can make:

A shallow copy, which you create using the slicing operator ([:]), the .copy()
method, or the copy.copy() function.

A deep copy, which you can create using the copy.deepcopy() function
"""

"""
When you make a shallow copy of an existing list, you create a new list of
objects with a different identity. However, the internal components or data
items in the new list are just aliases of those in the original list.

if you make a deep copy, then you create a completely
new copy of the original list.
"""


matrix = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]

shallow_copy = copy.copy(matrix)
deep_copy = copy.deepcopy(matrix)

print(id(matrix))


print(id(shallow_copy))


print(id(deep_copy))

"""
Here we are checking the value are equal or not
The == operator is checking the id of first matrix
is equal to the shallow_copy's first matrix.
In this case we will have same id for both list
as we are pointing to same address in memory. which
is also known as aliasing.


In the second case we are deep copying everything
meaning we are copying every element and value and
assigning to the new memory address.
meaning whenever we change anything inside the deep copy
or check id we won't change the orginal value.
"""
print(id(matrix[0]) == id(shallow_copy[0]))
print(id(matrix[0]) == id(deep_copy[0]))
matrix[1][1] = 555
print(matrix)
print(shallow_copy)
print(deep_copy)

"""
Getting None From Mutator Methods

When you do any mutation on immutable value you will
get a copy of new value, now this helps you to chain the
methods and apply changes on each copy of new data.
"""
text = '<html lang="en">'

print(text.removeprefix("<").removesuffix(">").upper().center(20))

"""
When it comes to the mutable value you will be peforming
changes in the data itself and you won't be getting any
value returned as output. suppose you call .sort() to
a list and try to print the output. You will get the None
"""
numbers = [3, 4, 2, 6, 1]
sorted_numbers = numbers.sort()
print(sorted_numbers)

"""
Storing Mutable Objects in Tuples
If tupels are contains the list then the value inside the list is mutable
but you cannot mutate the items outside the list as well as the list
itself. here is an example.
"""
red = ("RED", [255, 0, 0])

print(type(red))

red[1][0] = 233

print(red)

"""
Here we were able to replace the value inside the tupel.
But why?
The thing is we are dealing with tupel but tupel has list
inside it and we know list are the mutable data type meaning everything
inside the list or values can be replaced.


What if we try to replace the "RED" to "GREEN"?
well for that we would have to access the the first element of
tupel the tupel won't let you modify it as it is not a mutable type.
"""
# red[0] = "Green" #  This will thorw an error as the tuple doesn't
# support the item assignment.
print(red)

"""
What if we try to modify the whole list?
Not the element inside the list?
"""

# red[1] = [1, 2, 3]


"""
This will also throw an error. Why?
Becuase the list is also an item inside the tupel, and element of tupel
cannot be modified
"""

"""
In general, putting mutable objects in tuples is a bad idea.
It kind of breaks the tuple’s immutability.
It also makes your tuples unhashable, which prevents you from using
them as dictionary keys
"""

"""
Concatenating Many Strings
"""
multiple_strings = "Hello" + "," + " " + "World" + "!"
print(multiple_strings)

"""
Here we are creating multiple strings as temporary variables
String is Immutable and While using + we are creating a new
copy of each sting.
"""
"""
Better alternative will be using .join method of string.
Join accepts the iterables as input and is efficient in
doing the concatination.
"""
using_joined = "".join(["Hello", ",", " ", "World", "!"])
print(using_joined)


"""
Mutability in Custom Classes

When you are creating a class they are mutable.
The user defined classes are mutable class.
You can mutate them in several ways.
- Add or delete class and instance attributes dynamically
- Change or reassign the value of class and instance attributes
"""


class User:
    pass


print(dir(User))

"""
User inherits all these attributes from the object class
which is the default parent class of every Python class.
you can provide class attributes and methods dynamically using dot
notation and an assignment like in User.attr = value.
"""

"""
We are creating an attribute for our class using . operator
here we are creating an attribute called name to the class
we are then assigning Arjun as the value to our name attr.
"""
User.name = "Arjun"


"""
we are creating a function called init. This looks like the class's
dunder method but it's just a simple function in this step.
"""


def __init__(self, name, age):
    self.name = name
    self.age = age


"""
Here we are assigning our __init__ method to the classe's dunder method
meaning we are defining the __init__ function in two step. OR I should
say overriding the __init__ method.
"""

User.__init__ = __init__

print(dir(User))


"""
What just happened?

we have managd to create an instance of user,
we also assigned our custom __init__ method to the user.
We also managed to add values to the user.
"""
user = User("Arjun", 23)
print(user.name)
print(user.age)

"""
When we print user using dir() we can see our custom attrs i.e.
name and age are listed in the console.
"""
print(dir(user))

"""
Custom classes and their instances are mutable because
they keep their attributes and methods in a special
dictionary called .__dict__.
Both the class and the instance will have a .__dict__ dictionary:
"""

"""
When we print the __dict__ representation of our class User.
It will print the dict of the values and the arttributes
in our case we had defined the custom attribute called name
and assigned "Arjun" to that name. We can see that when we
print the dict of the class.
"""
print(User.__dict__)

"""
When we print the user where we created the object of User class.
We can see the name and age and their values, inside the dict.
"""
print(user.__dict__)


"""
The User.__dict__ dictionary is a private namespace for the class object.
There you’ll find class attributes and methods, such as .name and .__init__(),
respectively.
"""
"""
Similarly, user.__dict__ holds instance attributes and their values
for the current instance, user.
"""

"""
Finally, you can also delete an
attribute from a class or an instance using the del statement:
"""
del user.age
print(user.__dict__)

"""
TODO: more research on the magic methods.
"""

"""
Mutability of Attributes
The second dimension of class and instance mutability is the possibility of
changing the value of class and instance attributes, by either mutating them
or reassigning them.
"""


class Book:
    def __init__(self, title):
        self.title = title


thinking_fast_and_slow = Book("Thinking Fast")
thinking_fast_and_slow.title = "Thinking Fast & Slow"
print(thinking_fast_and_slow.title)


"""
what happened?
we first created the book with the title Thinking Fast
once that's done we again modified the title and appended
& Slow in the title
Classic Example of mutation.
"""

"""
Techniques to Control Mutability in Custom Classes.
Defining a .__slots__ class attribute
Providing custom .__setattr__() and .__delattr__() methods
Using read-only properties
Relying on descriptors with an appropriate .__set__() method
Using an immutable class, such as a named tuple or a data class
"""

"""
Defining a .__slots__ Class Attribute.
Python allows you to create classes that prevent the addition of
new instance attributes.
"""


class Book:
    __slots__ = ("title", )

    def __init__(self, title):
        self.title = title


"""
What does __slots__ do?
it won't let you create additional args which are not defined in
slots.
"""
new_book = Book("Testing")
print(new_book.title)
# new_book.new_arg = "arg"

"""
Unfortunately, the .__slots__ attribute doesn’t prevent you from adding new
class attributes and methods dynamically:
"""
Book.publisher = "Example"
print(dir(Book))


"""
Even if you define a .__slots__ attribute, you won’t be able to prevent your
users from removing allowed attributes from your class:
"""
del new_book.title
# print(new_book.title)


"""
Providing Custom .__setattr__() and .__delattr__() Methods
"""

"""
Python automatically calls the .__setattr__() method when you use an attribute
in an assignment statement. Similarly,
Python calls the .__delattr__() method when you run a del statement to remove a
given attribute.
"""

"""
You can provide your own implementations of these methods to prevent these
mutations from happening in your classes:
"""


class Immutable:
    def __init__(self, value):
        super().__setattr__("value", value)

    def __setattr__(self, name, attr_value):
        raise AttributeError(f"can't set attribute '{name}'")

    def __delattr__(self, name):
        raise AttributeError(f"can't delete attribute '{name}'")


gravity = Immutable(9.78)
print(gravity.value)

# gravity.value = 9.8


"""
This class provides custom implementations of .__setattr__() and .__delattr__()
The former raises an AttributeError when you try to change the value of an
existing attribute or when you try to add a new one.

Similarly, the .__delattr__() method raises an AttributeError when you try to
delete the .value attribute using the del statement.
"""

fruits = Immutable(["apple", "orange", "banana"])
print(fruits.value)

# fruits.value = 42

fruits.value.append("lemon")
print(fruits.value)


del fruits.value[0]
print(fruits.value)

"""
In this example, you can’t reassign .value to hold the number 42 because your
class is immutable in that sense. However, you can change the current value of
this attribute because the contained object is mutable.

In this regard, your Immutable class behaves similarly to Python tuples, which
are immutable by definition but can store mutable objects that you can mutate
at will.
"""

