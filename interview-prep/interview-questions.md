
### Python's memory management mechanisms
1. Why does Python use a reference counting system, and how does it handle cyclic references?<br>
       Python uses reference counting to manage memory because it is simple and efficient for most cases.
       Every object in Python has a reference count, which is incremented when an object is referenced
       and decremented when it’s dereferenced. When the count reaches zero, the memory is released.
       However, cyclic references (e.g., objects referring to each other) can't be cleaned up by
       reference counting alone, so Python also employs a garbage collector that detects and
       handles cycles using a generational approach.<br>

2. What is the role of the Garbage Collector in Python, and how would you control or configure it?<br>
    Python's garbage collector supplements reference counting by identifying and cleaning up cyclic references.
    It operates using generations—young objects are collected frequently, while older objects are collected less often.
    You can control it using the gc module by enabling/disabling it, triggering collections manually,
    or adjusting thresholds using gc.set_threshold().<br>

### Global Interpreter Lock (GIL)
1. Why does Python have a GIL, and how does it affect multithreading in CPython? <br>
    The GIL is a mutex that prevents multiple native threads from executing Python bytecodes concurrently in CPython.
    It exists due to limitations in CPython’s memory management, specifically to avoid race conditions when managing reference counts.
    The GIL simplifies memory management but limits the performance of CPU-bound programs, as threads can't run in true parallel.<br>

2. What techniques would you use to optimize performance when dealing with CPU-bound tasks? <br>
    For CPU-bound tasks, multithreading won’t help much due to the GIL. Instead,
    I would use multiprocessing, which creates separate memory spaces and bypasses the GIL.
    Another option is to offload performance-critical code to
    C extensions or use NumPy for optimized numerical computations.<br>

### Python's exceptions under the hood
1. Why is exception handling slower than normal control flow, and what impact does this have on performance? <br>
    Python's exception handling is slower because raising an exception involves the interpreter stopping the normal flow,
    creating an exception object, unwinding the call stack, and then locating an appropriate handler.
    This process is more resource-intensive compared to a simple if check, 
    impacting performance in high-frequency error-prone code paths.<br>

2. What happens when an exception is raised but not caught in Python?
    When an exception is raised but not caught, Python unwinds the stack and prints a traceback to the console,
    showing where the exception occurred. If no handler is found, the program terminates.<br>

### Python’s meta-classes
1. Why would you use a metaclass instead of a class?
    Metaclasses allow you to control the creation of classes themselves.
    You use metaclasses when you need to modify class behavior, enforce coding standards, or add functionality during class creation.
    For example, a metaclass can automatically register subclasses or modify class attributes dynamically.<br>

2. What is the difference between a class and a metaclass?<br>
    A class is a blueprint that defines the structure and behavior of an object.
    A metaclass is a class that defines the behavior of a class. Both are used to create classes dynamically.<br>

3. How do metaclasses work in Python, and what are some practical use cases?<br>
   Metaclasses are defined using class Meta(type). When a class is created, its metaclass’s __new__ or __init__ method is called. 
   Practical use cases include creating singleton patterns, class registries, or ORM systems where classes need to be dynamically modified at runtime.

### Python’s asyncio module
1. Why would you use asynchronous programming, and what are the main limitations of Python’s asyncio?<br>
    Asynchronous programming is useful for I/O-bound tasks where waiting (e.g., for a network response) can be optimized 
    using non-blocking operations. asyncio allows you to run such tasks concurrently without creating multiple
    threads or processes. However, asyncio does not help with CPU-bound tasks and still runs in a single thread,
    making it unsuitable for parallel computation.<br>

2. How does Python internally handle coroutines, and what are the differences between async and threading for I/O-bound tasks?
   Coroutines are functions declared with async def and can be paused and resumed using await. 
   The event loop in asyncio schedules coroutines and handles their execution. Unlike threads, 
   coroutines don’t have the overhead of context switching and can be more efficient for I/O-bound tasks, 
   whereas threading incurs more overhead due to the GIL and locking mechanisms.<br>


### Python namespaces and scope resolution
1. Why is the LEGB (Local, Enclosing, Global, Built-in) rule important, and what are its implications for variable scoping?<br>
    The LEGB rule defines the order in which Python resolves variable names. 
    First, it checks the local scope, then the enclosing scopes (for nested functions), followed by the global scope, 
    and finally, the built-in scope. This ensures that variables in closer scopes take precedence, which can sometimes 
    lead to shadowing if a variable in an inner scope has the same name as one in an outer scope.<br>

2. How would you resolve naming conflicts or ensure proper namespace management in large applications?<br>
   To avoid naming conflicts, I would use namespacing with modules and packages, and adopt clear and descriptive 
   variable naming conventions. In some cases, explicitly using global or nonlocal keywords can help with scope 
   resolution, although it’s generally better to avoid modifying variables from outer scopes directly.<br>

### deep copy and shallow copy in Python
1. How do they differ in terms of object mutability and memory usage?<br>
   A shallow copy creates a new object but does not recursively copy objects contained within the original. 
   It merely copies references to those objects. A deep copy, on the other hand, creates new copies of all objects,
   recursively copying even the nested objects.
   Mutable objects in a shallow copy can lead to unexpected behavior since
   changes to the nested objects will affect both copies.<br>
2. Why would you choose one over the other in real-world scenarios?<br>
   Use a shallow copy when the nested objects are immutable or when you want to retain shared state between copies. 
   A deep copy is needed when you require complete independence between the copied objects to avoid unintended side effects.<br>




