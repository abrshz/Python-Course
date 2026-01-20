# Data Types 

# Primitive Data types of Python 

# 1) Numeric Types are used to represent numbers. 

# - Integers(int):- Whole numbers, positive or negative, without decimals. E.g:- 5, -56 
print(type(-67)) # int
# - float:- Numbers containing one or more decimals. E.g:- 3.14 , -2.5
print(type(-2.5)) # float
# - complex:- Numbers written with a "j" as the imaginary part. E.g 8 + 5j 
print(type(3+5j)) # complex 

# 2) Sequence Types allow you to store multiple values in an organized, indexed manner. 

# str (String): A sequence of Unicode characters wrapped in quotes (e.g., "Hello World").

# list: An ordered, mutable (changeable) collection that allows duplicate members (e.g., [1, "apple", 3.5]).
print(type([1, "apple", 3.5])) # list
# tuple: An ordered, immutable (unchangeable) collection that allows duplicate members (e.g., (10, 20, 30)).
print(type((10,20,30,40))) # tuple
# range: Represents a sequence of numbers, commonly used for looping (e.g., range(6)).
print(type(range(5))) # range 
# 3) Mapping Type use to store data in key value pairs.

# dict (Dictionary): A collection which is ordered (as of Python 3.7+) and changeable. No duplicate keys allowed (e.g., {"name": "Alice", "age": 25}).
print(type({"name": "Alice", "age": 25}))
# 4) Set Types used to store collections of unique items. 

# set: An unordered, unindexed collection of unique items (e.g., {"apple", "banana", "cherry"}).
print(type({"apple", "banana", "cherry"}))
# frozenset: An immutable version of a set.

# 5) Booleans Type used to represent truth or false values. 

# 6) Binary Types used for manipulating binary data (bytes). 
 
# bytes: Immutable sequences of single bytes (e.g., b"Hello").

# bytearray: A mutable version of bytes.

# memoryview: Allows Python code to access the internal data of an object that supports the buffer protocol without copying.

# 7. None Type represents the absence of a value or a null value, denoted by the keyword None.

# To check any data type use type 

print(type(len("345678")))

# print('Number of letter in your name: ' , len(input('Enter your name: ')))

# Mathematical Operations 

# Basic mathematical operations are + , - , * , / 

# Examples

print(16 / 2) # float
print(8//4) # Integer 
print(5**3) # Power 

# PEMDAS:- Parentheses , Exponents , Multiplication , Division , Addition , Subtraction 

print(3*3+3/3-3) # Output 7

print(3*3/3+3-3) # Output 3

# Number manipulation use int() function method
# round() function method use to round the float number. 
# E.g: 
print(round(3.1345, 3))
print(6 + 4 / 2 - (1 * 2))
a = int("5") / int(2.7)
print(type(a))










