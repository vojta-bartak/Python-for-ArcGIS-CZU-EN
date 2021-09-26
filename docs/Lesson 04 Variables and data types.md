# Lesson 4: Variables and data types

## Variables

In Python, a variable is a reference to an object in RAM. This object can be of various types (or classes): it can be a number, a text string, or anything else (see below). The variable has some name (chosen by us) and some value. We assign a value to a variable with the `=` operator:

```python
>>> a = 5
```

The data type of a variable can be found by the *type* function:

```python
>>> type(a)
<type 'int'>
>>> b = "Hello world"
>>> type(b)
<type 'str'>
```

> The concept of *function* will be thoroughly discussed later. So far, it is enough to understand that when calling a function, we always write its name, and in the brackets after the name we paste its *arguments*, ie some values ​​with which the function does something. The function usually *returns* something, ie its result is a value (object). So whenever you see simple brackets behind a name, you're dealing with a function.

You can "store" the value of another variable in a variable:

```python
>>> a = 5
>>> b = a
>>> b
5
```

However, it is important to understand that if we change the value of the original variable, the value of the new variable remains unchanged (this variable still refers to the original object - in our case number 5 - while the original variable now refers to another object, eg number 100):

```python
>>> a = 100
>>> b
5
```

Variables can have almost any name, but the following rules must be met:

- The name starts with an English alphabet letter or an underscore.
- Any sequence of numbers, English letters, and/or underscores can follow.
- The name must not be a language keyword (e.g. `and` or` if`).
- Lowercase and uppercase letters are differentiated (ie Python is **case sensitive**).

Python also allows the following weird thing (creating two or more variables at once):

```python
>>> a, b = 3, 5
>>> a
3
>>> b
5
```

> **Task 1.** Try to create several variables of different names and verify their behavior described above.

An existing variable can also be deleted using the `del` command:

```python
>>> x = 5
>>> x
5
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell # 5>", line 1, in <module>
    x
NameError: name 'x' is not defined
```

## Numbers

There are two basic data types for numbers in Python. These are integer numbers (*integers*, abbreviated to *int*):

```python
>>> 56
56
>>> -32586
-32586
```

and decimal numbers (*floating point numbers*, abbreviated to *float*):

```python
>>> 5.32
5.32
>>> -6e-7
-6e-7
>>> -5.0E-4
-0.0005
```

Common mathematical operations can be performed on numbers using arithmetic operators:

```python
>>> 3 + 2 # Addition
5
>>> 3 - 2 # Subtraction
1
>>> 3 * 2 # Multiplication
6
>>> 3/2 # Integer division of integers
1
>>> 3.0 / 2 # Division
1.5
>>> 3.1 // 2 # Integer division of floating point numbers
1.0
>>> 3 ** 2 # Power
9
>>> 3% 2 # Modulo (remainder after integer division)
1
```

The numeric type of the result is always determined by the numeric type of the input numbers: if the inputs are only integers, the result is an integer (when dividing, an integer division is performed); if at least one of the inputs is a decimal number, the result is also a decimal number.

Python has a number of built-in math functions (there are only a few in the example):

```python
>>> abs(-5) # Absolute value
5
>>> max(5,3,-5,1) # Maximum
5
>>> min(5,3,-5,1) # Minimum
-5
>>> pow(2,3) # Power (equivalent to 2 ** 3)
8
>>> round(5.6) # Rounding
6.0
>>> round(5.627,2) # Rounding to two decimal places
5.63
```

Additional math functions can be found in the `math` module:

```python
>>> import math # Load the math module
>>> math.pi # Approximation of the number pi
3.141592653589793
>>> math.sqrt (2) # Square root
1.4142135623730951
>>> math.log (math.exp(1)) # Logarithm and exponential
1.0
```

You can convert between individual number types:

```python
>>> a = 5.6
>>> type(a)
<type 'float'>
>>> b = int(a) # Conversion to integer
>>> b
5
>>> type(b)
<type 'int'>
>>> c = float(b) # Conversion to a decimal number
>>> c
5.0
>>> type(c)
<type 'float'>
```

Similarly, you can convert between other data types:

```python
>>> int("56") # Convert text to an integer
56
>>> float("56") # Convert text to a decimal number
56.0
>>> str(56) # Convert number to text
'56'
```

> **Task 2.** Try all the above operations and commands.

## Text strings

Text strings (or *string*) are written either in quotation marks or in apostrophes:

```python
>>> a = "This is a text string that can contain the character ',"
>>> b = 'and this is a string that can contain the character ".'
>>> print (a); print (b)
This is a text string that can contain the character ',
and this is a string that can contain the character ".
```

A third way to create a string is to use triple quotation marks. It is then possible to insert more lines into such a string (without having to use a special character for the end of line):

```python
>>> a = """This is a text string,
which contains
three lines"""
>>> print a
This is a text string,
which contains
three lines
```

Strings can to some extent be understood as sequences of individual characters. In Python, strings are indexed, which means that you can, for example, read a specific (for example, the fifth) character directly:

```python
>>> a = "From this string I will read the fifth character:"
>>> print a[4]
h
```

Indexing in Python starts with zero, not one, so it was necessary to write index 4 in square brackets to print the fifth character.

In addition to accessing individual characters, you can also use square brackets and indexes to create so-called *slices*, or read only a certain part of a string:

```python
>>> a = "I will make slices from this string:"
>>> print a[2:11]
will make
>>> print a[:18]
I will make slices
>>> print a [7:]
make slices from this string:
```

Slices are done according the following rules:

- A slice starts with en element at the position of the first index, and ends at the last position before the second index (ie the element corresponding to the second index is **not** included in the slide). The section `a[2:10]` thus contains the third to tenth characters.
- A slice with an empty first index contains the entire original string from the beginning to the character at the position before the second index.
- A slice with an empty second index contains the entire original string starting with the character at the position of the first index.

Strings (unlike lists) cannot be overwritten using indexing and slices. E.g. if we want to change the first letter to "f" in the text "rat", this cannot be done directly:

```python
>>> a = "rat"
>>> a[0] = "f"
Traceback (most recent call last):
  File "<pyshell # 57>", line 1, in <module>
    a[0] = "f"
TypeError: 'str' object does not support item assignment
```

Strings can be added and multiplied by a natural number using the `+` and `*` operators:

```python
>>> a = "Hello "
>>> b = "World"
>>> print a + b
HelloWorld
>>> print a + " " + b + "!"
Hello World!
>>> print a * 5
HelloHelloHelloHelloHello
```

You can change the above-mentioned "rat" to "fat", for example, as follows:

```python
>>> a = "rat"
>>> a = "f" + a[1:]
>>> print a
fat
```

The string can contain so-called *escape sequences*, ie sequences of characters having a special meaning. The escape sequence is always preceded by a backslash `\`:

```python
>>> print '\''# Apostrophe character in a string defined by apostrophes
'
>>> print "\""# Quotation mark in a string defined by quotation marks
"
>>> print "Here is \ttabulator" # Tabulator character
Here is     tabulator
>>> print "Here is \nnew line" # End of line character
Here is
new line
```

Because escape sequences are preceded by a backslash, the backslash itself cannot be used in the text:

```python
>>> print(In this text I try to use the character \")
SyntaxError: EOL while scanning string literal
```

This can be solved by using a double backslash, which is another of the escape sequences:

```python
>>> print ("In this text I try to use the character \\")
In this text I try to use the character \
```

This is especially important when writing directory and file addresses where backslashes are used:

```python
>>> print "C:\\Users\\MyComputer\\Documents"
C:\Users\MyComputer\Documents
```

Another way to write addresses is to use a forward slash:

```python
>>> print "C:/Users/Muj_pocitac/Documents"
C:/Users/MyComputer/Documents
```

Yet another way is to start the string with the `r` character (before the quotation marks). This shows that it is a so-called *raw string*, in which all characters are to be read in their usual way (the backslash is therefore only a backslash and there can be no escape sequences):

```python
>>> print r"C:\Users\MyComputer\Documents"
C:\Users\MyComputer\Documents
```

## Lists

A list is a sequence of arbitrary objects. It is defined using square brackets and its items are separated by commas:

```python
>>> list1 = [2,-4,56,105,0]
>>> list2 = ["hello", "TREE", "", "guru"]
```

Values ​​of different data types can be stored in one list (this is not customary in other programming languages):

```python
>>> list3 = [0, "hello", - 5.78, 2, 4]
```

As was the case with text strings, individual list items can be accessed using indexes:

```python
>>> list3[3]
2
```

Indexes start with zero (ie the first item in the list has an index of 0, not 1!), and negative indexes can be used. Negative indexes index the list from the end, ie the last element of the list has an index of -1, the previous one -2, etc. Negative indexing is especially advantageous for a quick access to the last item of the list without knowing or referring to the list length:

```python
>>> list3[-1]
4
```

Unlike for text strings, individual items of lists can changed using indexes:

```python
>>> list1[2] = "new value"
>>> list1
[2, -4, 'new value', 105, 0]
```

A list slice is a list that consists only of some elements of the original list. It is created using square brackets, two indices (start and end of the slice) and a colon between them:

```python
>>> list2 [1: 4]
['TREE', '', 'guru']
```

As can be seen from the example, the element at the position of the second index is **not** included in the slice. Negative indices can also be used in a slide, so for example a slide

```python
>>> list2[0: -1]
['hello', 'TREE', '']
```

contains all elements from the first to the penultimate.

If we leave one of the indexes empty, the slide is made from the beginning resp. to the end of the list:

```python
# this is the slide from the beginning of the list to the third element:
>>> list2[:3]
['hello', 'TREE', '']

# this is the slide from the second element to the end of the list:
>>> list2[1:]
['TREE', '', 'guru']

# this is the so-called full slice:
>>> list2[:]
['hi', 'TREE', '', 'guru']
```

Another way to create slices is to use a third "index", or rather a value, that determines the step length when selecting elements for a slice. In this way, for example, you can create a slice containing every second (or third) number from a certain range:

```python
>>> a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
>>> a [2:10:2]
[3, 5, 7, 9]
>>> a [1:13:2]
[2, 4, 6, 8, 10, 12]
>>> a [::3]
[1, 4, 7, 10, 13, 16]
```

As with strings, lists can be joined by addition and multiplied by a natural number (including zero):

```python
>>> list1 + list2
[2, -4, 'new value', 105, 0, 'hello', 'TREE', '', 'guru']
>>> list1*2
[2, -4, 'new value', 105, 0, 2, -4, 'new value', 105, 0]
>>> 0*list2
[]
```

Multiplying the list by zero (as well as any negative integer) results in an empty list.

Just as individual list items can be rewritten using indexes, entire slices can also be rewritten, with a list of any length:

```python
>>> a = [1,2,3,4,5]
>>> a [:3] = ["one", "two", "three", "three and a half"]
>>> a
['one', 'two', 'three', 'three and a half', 4, 5]
```

In this way, you can add any items to the end of a list (note that in this case you can use an index that is already outside the range of the original list):

```python
>>> a [6:] = [6]
>>> a
['one', 'two', 'three', 'three and a half', 4, 5, 6]
```

or to its beginning:

```python
>>> a [:0] = [-1.0]
>>> a
[-1.0, 'one', 'two', 'three', 'three and a half', 4, 5, 6]
`` `

or anywhere in the middle of the list:

```python
>>> a [3:3] = [1.5]
>>> a
[-1.0, 'one', 1.5, 'two', 'three', 'three and a half', 4, 5, 6]
```

You can also delete part of the list by inserting an empty list:

```python
>>> a [4:7] = []
>>> a
[-1.0, 'one', 1.5, 4, 5, 6]
```

In the section about variables, we explained that a variable is a reference to an object in RAM. A variable `a = [1,2,3]` is therefore a reference to the corresponding object-list. However, this means that if I create a variable `b = a`, this new variable will refer to the same object. Of course, if I now change this object through one of the variables, the change will of course affect the other variable as well:

```python
>>> a = [1,2,3]
>>> b = a
>>> a[0] = -50
>>> a
[-50, 2, 3]
>>> b
[-50, 2, 3]
`` `

If we want to make an independent copy of the list, we can use the full slice:

```python
>>> a = [1,2,3]
>>> b = a[:]
>>> a[0] = -50
>>> a
[-50, 2, 3]
>>> b
[1, 2, 3]
```

In addition to the above options for working with lists using mathematical operators and slices, there are so-called *list methods* in Python, which are functions that are called using a list name, a dot, and the name of a method:

```python
>>> x = [1,2,3]

# Add a new element to the end of the list using the append method
>>> x.append("hello")
>>> x
[1, 2, 3, 'hello']

# Insert an element at a given position in the list using the insert method
>>> x.insert(1, 1.5) # Inserts the value 1.5 in the second position (ie with index 1)
>>> x
[1, 1.5, 2, 3, 'hi']

# Sort a list of numbers or text strings using the sort method
>>> x = [2, 9, -13, 0, 50]
>>> x.sort()
>>> x
[-13, 0, 2, 9, 50]
>>> x = ["hello", "bread", "coffee", "lighter", "sticks", "breakfast"]
>>> x.sort()
>>> x
['bread', 'breakfast', 'coffee', 'hello', 'lighter', 'sticks']

# Find the index of a given value using the index method
>>> x.index("lighter")
4

# Find out how many times a given value appears in the list using the count method
>>> x.count("lighter")
1

# Delete the first occurrence of a given value with the remove method
>>> x.remove("lighter")
>>> x
['bread', 'breakfast', 'coffee', 'hello', 'sticks']

# Reverse the order of values ​​in a list using the reverse method
>>> x.reverse()
>>> x
['sticks', 'hello', 'coffee', 'breakfast', 'bread']
```

In addition to list methods, there are other built-in functions in Python that you can use to work with lists (these functions can be used just as well for strings):

```python
>>> a = [1,2,3]

# Find the length of a list
>>> len(a)
3

# Finding the smallest and largest element of a list using min and max functions
>>> min(a)
1
>>> max(a)
3

# Deleting part of the list using del functions
>>> a = [1,2,3,4,5]
>>> del(a[2])
>>> a
[1, 2, 4, 5]
>>> del[:2]
>>> a
[4, 5]

```

It is possible to insert other lists (so-called *nested lists*) into a list and thus create a list of lists, or list of lists of lists, etc.:

```python
>>> a = [1, "hello", [1,2,3], ["a", "b"]]
>>> a[2]
[1, 2, 3]
>>> a[3]
['a', 'b']
>>> a[3][0]
'a'
```

The nesting depth can be considerable (practically unlimited):

```python
>>> a = [[[[[1]]]]]
>>> a[0]
[[[[1]]]]
>>> a[0][0]
[[[1]]]
>>> a[0][0][0]
[[1]]
>>> a[0][0][0][0]
[1]
>>> a[0][0][0][0][0]
1
```

## Tuples and dictionaries

*Tuple* is a structure similar in all ways to lists, except that it cannot be directly changed using indexes. In contrast to lists, it is written using *round* brackets:

```python
>>> a = (1,2,3)
>>> a[1]
2
>>> a[1] = 4
Traceback (most recent call last):
  File "<pyshell # 43>", line 1, in <module>
    a[1] = 4
TypeError: 'tuple' object does not support item assignment
```

The reason why tuples exist and how they differ from lists in practice will be explained later.

Another data type similar to list is *dictionary*. A dictionary can be thought of as a list of named items. Item names are called *keys*. Each dictionary entry thus consists of a pair of a *key* and its corresponding *value*. The dictionary is written with curly brackets, the individual items are separated by commas, and the key is separated from the corresponding value by a colon:

```python
>>> person = {"name": "Charles", "age": 60, "childern": 3}
>>> person
{'age': 60, 'name': 'Charles', 'childern': 3}
`` `

The basic difference between dictionaries and lists is that in the dictionary, individual items are accessed not by indexes, but using the keys:

```python
>>> person['name']
'Charles'
>>> person['age']
60
```

List of values ​​resp. keys of the dictionary can be obtained using the `values` resp. `keys` method:

```python
>>> person.keys()
['age', 'name', 'childern']
>>> person.values​​()
[60, 'Charles', 3]
```

Dictionaries are a very useful part of the Python language, and their use go far beyond this small example. However, we will not work with them much in this course, so we leave the deeper acquaintance with them to the reader.

## Logical values

There are two logical values: *true* and *false*. Most programming languages, with the exception of Python, have a special data type to represent these two values. This data type is usually called *Boolean*, in honor of the famous 19th century British mathematician George Bool, who has made a significant contribution to the development of mathematical logic and is sometimes referred to as the ancestor of computer science.

In python, the data type `bool` is directly derived from the data type `int`, ie integers. The value `True` is actually an integer value `1` (and can be represented by it), while the value `False` corresponds to the number `0` (and can also be represented by it). The result is, for example, that the values ​​`True` and `False` can be part of arithmetic expressions with numbers:

```python
>>> True + 1
2
>>> False * 3
0
```

The great advantage of Python is that it is able to interpret essentially any value of any data type as a logical value. What is the logical value of a value can be easily determined using the conversion function `bool`:

```python
>>> bool(0)
False
>>> bool(5)
True
>>> bool(0.0)
False
>>> bool(-7.0)
True
>>> bool("")
False
>>> bool("Hello")
True
>>> bool([])
False
>>> bool([1,2,3])
True
```

Logical value is also a result of comparison operations:

```python
>>> 5 > 3
True
>>> 5 <= 3
False
>>> "a" == "a"
True
```

## Value `None`

In Python, as in most other languages, there is a special value representing *nothing*, or an empty value. An empty value exists in Python as a `None` data object, which can be thought of as a value that can be assigned to any variable:

```python
>>> a = None
>>> a
>>>
```

After entering the variable name, "None" is not displayed, but really nothing is displayed. A variable does exist, but it contains nothing. In fact, when Python starts, a `None` data object is created in the computer's operating memory, to which all the variables to which the` None` value is assigned refer (so there is always only one "nothing", no matter how many variables contain it).

The logical value of `None` is `False`:

```python
>>> bool(None)
False
```

## Summary

In this chapter, you learned about the basic rules for working with variables and the basic data types of Python.

## Exercises