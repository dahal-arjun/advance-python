"""
What is a Class?
A class is a blueprint for creating objects. It defines the properties and
methods that the objects created from the class will have. It is a logical
representation of real-world objects.

What is an Object?
An object is an instance of a class. It is a specific realization of a class.

Why OOP?
Organization:
OOP defines well known and standard ways of describing and
defining both data and procedure in code. Both data and procedure can be
stored at varying levels of definition (in different classes),
and there are standard ways of talking about these definitions.
That is, if you use OOP in a standard way, it will help your later self
and others understand, edit, and use your code. Also, instead of using a complex,
arbitrary data storage mechanism (
dicts of dicts or lists or dicts or lists of dicts of sets, or whatever),
you can name pieces of data structures and conveniently refer to them.

State:
OOP helps you define and keep track of state.
For instance, in a classic example, if you're
creating a program that processes students (for instance, a grade program),
you can keep all the info you need about them in one spot
(name, age, gender, grade level, courses, grades, teachers,
peers, diet, special needs, etc.),
and this data is persisted as long as the object is alive,
and is easily accessible. In contrast, in pure functional programming,
state is never mutated in place.

Encapsulation:
With encapsulation, procedure and data are stored together.
Methods (an OOP term for functions) are defined right alongside the data
that they operate on and produce. In a language like Java that allows for
access control, or in Python, depending upon how you describe your public API,
this means that methods and data can be hidden from the user.
What this means is that if you need or want to change code,
you can do whatever you want to the implementation of the code,
but keep the public APIs the same.

Inheritance:
Inheritance allows you to define data and procedure in one place (in one class),
and then override or extend that functionality later. For instance,
in Python, I often see people creating subclasses of the dict
class in order to add additional functionality.
A common change is overriding the method that throws an exception
when a key is requested from a dictionary that doesn't exist to
give a default value based on an unknown key.
This allows you to extend your own code now or later, allow others to extend
your code, and allows you to extend other people's code.

Reusability:
All of these reasons and others allow for greater reusability of code.
Object-oriented code allows you to write solid (tested) code once,
and then reuse over and over.
If you need to tweak something for your specific use case,
you can inherit from an existing class and overwrite the existing behavior.
If you need to change something, you can change it all while maintaining
the existing public method signatures, and no one is the wiser (hopefully).


"""

"""
Let's now learn to create a class in python
https://docs.python.org/3/tutorial/classes.html (reference)

Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made.
Each class instance can have attributes attached to it for maintaining its state.
Class instances can also have methods (defined by its class) for modifying its state.

Keep this in mind::
Objects can contain arbitrary amounts and kinds of data. As is true for modules, classes partake of the dynamic nature
of Python: they are created at runtime, and can be modified further after creation.

Before introducing classes, I first have to tell you something about Python’s scope rules. Class definitions play some
neat tricks with namespaces, and you need to know how scopes and namespaces work to fully understand what’s going on.
Incidentally, knowledge about this subject is useful for any advanced Python programmer.
"""


"""
A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but
that’s normally not noticeable in any way (except for performance), and it may change in the future. Examples of
namespaces are: the set of built-in names (containing functions such as abs(), and built-in exception names); the global
names in a module; and the local names in a function invocation. In a sense the set of attributes of an object also
form a namespace. The important thing to know about namespaces is that there is absolutely no relation between names in
different namespaces; for instance, two different modules may both define a function maximize without confusion —
users of the modules must prefix it with the module name.

The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted.
The global namespace for a module is created when the module definition is read in; normally,
module namespaces also last until the interpreter quits.

The local namespace for a function is created when the function is called, and is deleted when the function returns.

A special quirk of Python is that – if no global or nonlocal statement is in effect – assignments to names always go
into the innermost scope. Assignments do not copy data — they just bind names to objects. The same is true for
deletions: the statement del x removes the binding of x from the namespace referenced by the local scope.
In fact, all operations that introduce new names use the local scope: in particular, import statements and function
definitions bind the module or function name in the local scope.

The global statement can be used to indicate that particular variables live in the global scope and should be rebound
there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there
"""

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"


    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)

class SampleClass:
    ''' A Simple class'''
    i = 12345

    def f(self):
        return 'hello world'



def __init__(self):
    self.data = []

SampleClass.__init__ = __init__

x = SampleClass()


'''
Found this section a bit long will continue it later.
The general concept is convered there above will look into the modifiers, access control
and other stuffs in future while continuing the series.
'''
