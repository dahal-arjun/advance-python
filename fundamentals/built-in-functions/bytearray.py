"""
the bytearray class is a mutable sequence of integrers in the range 0
<= x < 256. It has most of the usual methods of mutable sequences,
described in Mutable Sequence Types, as well as most methods that bytes
type has.

"""
print(bytearray(b'byte array of string'))

my_string = "Hello World"
my_bytes = bytearray(my_string, "utf-8")
new_string = my_bytes.decode("utf-8")
print(new_string)
