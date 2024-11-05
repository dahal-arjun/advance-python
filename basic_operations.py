# from beginner to advance level of comprehension concepts
import math
# Square each number
lst = [1, 2, 3, 4, 5]

print([a * a for a in lst])


# Filter even numbers
print([a for a in lst if a % 2 == 0])


# Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30]
print([c * (9/5)+32 for c in celsius])


# Convert to Upper Case
words = ['apple', 'banana', 'cherry']

print([word.upper() for word in words])

# Extract the first letter of each word
words = ['hello', 'world', 'python']
print([a[0] for a in words])


# Add 5 to each element in a list
lst = [1, 2, 3, 4]
print([a+5 for a in lst])


# Filter words by length
# create a new list with only the words that have more than three letters
words = ['sun', 'moon', 'sky', 'stars']
print([word for word in words if len(word) > 3])

# Generate odd numbers up to a given number
n = 10
print([a for a in range(n) if a % 2 == 1])

# Find the length of the words of the given list
words = ['apple', 'banana', 'cherry']
print([len(a) for a in words])


# List of only positive integers
numbers = [-2, -1, 0, 1, 2]
print([a for a in numbers if a > 0])

# Reverse the string
words = ['abc', 'def', 'ghi']
print([a[::-1] for a in words])


# Create a list of boolean values if the number is greater than 5
lst = [3, 5, 7, 9]
print([a > 5 for a in lst])

# Remove vowels from a list of words
words = ['apple', 'banana', 'cherry']
vowels = "aeiou"
print([''.join([char for char in word if char.lower() not in vowels])
      for word in words])


# Intermediate and advance
# Given a list of words, filter out those that contain the letter 'a'.
words = ['apple', 'banana', 'cherry', 'date']
print([a for a in words if 'a' in a])

# Given a list, create a list of tuples where each tuple contains the index and
# the value of each item.
lst = ['a', 'b', 'c']
print([(i, a) for i, a in enumerate(lst)])

# Flatten a nested list
# Given a list of lists, flatten it into a single list.
nested_lst = [[1, 2], [3, 4], [5, 6]]
print([item for row in nested_lst for item in row])


# Get unique characters from a string Use a set comprehension to get all unique
# characters from a string.
s = 'hello world'
print({char for char in s if char != ' '})

# Generate squares of even numbers within a range
# Create a list of squares for all even numbers between 1 and 20.
print([num**2 for num in range(1, 21) if num % 2 == 0])

# Filter dictionary based on conditions
# Given a dictionary with student names as keys and scores as values,
# use dictionary comprehension to filter out students who scored more than 80.
students = {'Alice': 90, 'Bob': 78, 'Charlie': 85, 'Diana': 92}
print({name: scrore for name, scrore in students.items() if scrore > 80})

# Transpose a Matrix
# Given a matrix, use list comprehension to transpose it
# (swap rows and columns).
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([list(col) for col in zip(*matrix)])


# Find the product of corresponding elements in two lists
# Given two lists of the same length, create a new list where each element
# isinstance the product of elements at the
# corresponding indicesin the two lists.

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

print([item1 * item2 for item1, item2 in zip(lst1, lst2)])


# Create a nested list of multiplication table
# Use list comprehension to generate a multiplication table
# (from 1x1 to 10x10) in the form of nested lists.
print([[i * j for j in range(1, 11)] for i in range(1, 11)])


# Filter out words with specific ending letters
# Given a list of words, create a new list containing only the words
# that end with the letter 'e'.
words = ['apple', 'orange', 'banana', 'grape', 'pineapple']
print([word for word in words if word[-1] == 'e'])

# Create a dictionary with square roots
# Given a list of numbers, create a dictionary where the keys are the numbers
# and the values are their square roots (rounded to 2 decimal places).
numbers = [4, 16, 25, 36]
print({num**2: math.sqrt(num) for num in numbers})

# Given a list of full names (first and last names), create a list with
# the initials of each person.
names = ['John Doe', 'Jane Smith', 'Alice Johnson']
print([''.join([word[0] for word in name.split(' ')]) for name in names])

# Given a list of words, create a dictionary where the keys are the
# words and the values are their lengths.
words = ['hello', 'world', 'python']
print({word: len(word) for word in words})

# Given a list of lists, where each sublist contains two elements
# [key, value], create a dictionary from it.
pairs = [['a', 1], ['b', 2], ['c', 3]]
print(dict(pairs))

# Given a sentence, create a dictionary that stores the frequency of each word.
sentence = "this is a test this is only a test"
print({word: sentence.split().count(word) for word in sentence.split()})
