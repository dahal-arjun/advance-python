import os


"""
The context management protocol allows you to create your own context managers
so you can customize the way you deal with system resources.

with statement helps you implement some common resource management patterns by
abstracting their functionality and allowing them to be factored out and reused
"""

"""
When you should use it?
One common problem you’ll face in programming is how to properly manage
external
resources, such as files, locks, and network connections. Sometimes, a program
will retain those resources forever, even if you no longer need them. This kind
of issue is called a memory leak because the available memory gets reduced
every
time you create and open a new instance of a given resource without closing an
existing one.
"""

"""
2 Approaches try finally and with
"""
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
finally:
    file.close()


file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    file.close()

with open("hello.txt", mode="w") as hello:
    hello.write("Hello Wrodld")

with open("hello.txt") as in_file, open("output.txt", "w") as out_file:
    info = in_file.read()
    info_upper = info.upper()
    out_file.write(info_upper)


with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name)


