# Lesson 7: Working with directories and text files

In this lesson, we will discuss how to handle the computer's directory structure in Python (setting up a working directory, creating directory paths, creating and deleting directories, etc.) and how to read and write text files. At the same time, we will show some additional tricks for working with text strings.

## Writing directory paths

In Python, the default way to write a directory path is the classic backslash style, such as `C:\MyFolder\my_file.txt`. The problem is that the backslash, as we know, has a special meaning in Python text strings (it introduces the *escape* sequence). There are three ways to work around this:

1. In the path notation, use forward slashes: `"C:/My_Folder/my_file.txt"`. Python can handle that.
2. Use the escape sequence `\\`, ie double backslashes: `"C:\\MyFolder\\my_file.txt"`. Both described methods are certainly advantageous if we want to list the routes manually. However, we often copy the path from a browser (or from another code) and then paste it into our code. Such paths tend to have backslashes, and their subsequent editing (replacement with forward or double backslashes) is lengthy and impractical. In this case, the third method is handy:
3. Before the text string, write `r` to create a "raw" string, all characters of which are interpreted as they are (ie the string does not contain any escape sequences): `r"C:\My_folder\my_file.txt"`.

An overview of all three methods:

```python
# Forward slashes
path = "C:/my_folder/my_file.txt"

# Double backslashes
path = "C:\\my_folder\\my_file.txt"

# Raw string
path = r"C:\my_folder\my_file.txt"
```

## `os` module

The module name is an abbreviation of the words "operating system". The module is designed for directory and process management. Of the many functions of the module, some of them will be especially useful for directory management. The `my_path` parameter has the meaning of a text string with a folder or file address in all examples.

Load the module in the standard way:

```python
import os
```

For operations with a directory structure, it is advantageous to have the so-called "workspace direcory" set correctly. If it is set, we do not have to enter the full path to files, for example, when entering input files into a calculation - if the input file is in the working directory, the Python interpreter will look for it there. Also, any output files, unless we specify the full path where they are to be saved, will be saved in the working directory. The default working directory setting depends on how we started IDLE:

- When opening an IDLE program in the standard way from the program menu, the working directory is set to the default position, typically `'C:\\WINDOWS\\system32'`. (For example, if we now want to open a script by pressing `Ctrl` + `O`, the search window will open in this location.)

- When opening the IDLE program "from a script", ie by opening the script for editing in the IDLE program, the working directory is automatically set to the folder with this script.

To find out the current working directory, use the `getcwd()` function (an aberviation of "current workspace directory"):

```python
>>> os.getcwd ()
'C:\\Documents and Settings\\MyComputer'
```

If, on the other hand, we want to change the working directory, we use the function `chdir(my_path)` (from "change directory"). Attention: the appropriate `my_path` location must exist!

```python
>>> os.chdir("C:/my_folder")
>>> os.getcwd()
'C:\\my_folder'
```

Often we want to perform some calculation in a cycle for all files in a folder, or for all folders in a parent folder. To get a list of items inside a folder, we use the `listdir(my_path)` function. The output list is a list of item names (ie strings), including suffixes (in an alphabetical order):

```python
>>> os.listdir("C:/my_folder")
['first_file.xls', 'last_file.txt', 'next_file.doc']
```

We often need to refer to the current working directory in similar functions (eg list its contents). This is possible with the already mentioned function `getcwd`:

```python
>>> os.listdir(getcwd())
['first_file.xls', 'last_file.txt', 'next_file.doc']
```

But there is an easier way. In Python, you can refer to the working directory by the abbreviation `"."`:

```python
>>> os.listdir(".")
['first_file.xls', 'last_file.txt', 'next_file.doc']
```

> **Task 1.** Change your working directory to a folder in which you have a large number of files of different types. Then write its contents on the console.


The other two functions that we will show are used to create new directories. The first, the `mkdir(my_path)` function, creates a new folder at the specified address. The condition is that the entire path except the end folder being created exists. This condition is bypassed by a second function, `makedirs(my_path)`, which creates a new folder at the specified address, including any non-existent parent folders.

```python
>>> os.mkdir ("C:/existing_parent_folder/new_folder")
>>> os.makedirs ("C:/new_parent_folder/new_folder")
```

If, on the other hand, we want to delete a folder or file, we have the following functions available:

```python
# Delete a file
>>> os.remove("C:/my_folder/my_file.doc")

# Delete an (empty!) folders
>>> os.rmdir("C:/empty_folder")

# Delete an (empty!) folder, including all (empty!) parent folders
>>> os.removedirs ("C:/empty_parent_folder/empty_folder")
```

The `rename(old, new)` and `renames(old_path, new_path)` functions are also useful, which can be used to rename file paths, thus not only renaming them, but also moving files to new locations. The first, `rename`, renames the target file from the old path to the new one, but the folder for the new file location must already exist. The second function, `renames`, does not require this and first creates the necessary non-existent folders in the new path (and at the same time removes the unnecessary folders of the original path).

```python
# Rename a file
os.listdir("C:/my_folder")
['first_file.xls', 'last_file.txt', 'next_file.doc']
os.rename("C:/my_folder/first_file.doc", "C:/my_folder/first_superfile.doc")
os.listdir("C:/my_folder")
['first_superfile.xls', 'last_file.txt', 'next_file.doc']

# Move a file
os.renames("C:/my_folder/next_file.doc", "C:/new_folder/moved_file.doc")
```

> **Task 2.** Save all text files (or files of another specific type) from your working directory to a newly created subfolder "`text_files`". Use a loop and an `if` condition.

## `os.path` module

The `os.path` module is a submodule of the `os` module, containing functions for working with the directory paths themselves. After loading the `os` module, the functions of the submodule are accessible via `os.path.some_function()`, but the submodule can also be loaded separately (then other functions from the `os` module will not be accessible):

```python
import os.path
```

eventual:

```python
from os import path
```

In the latter case, the submodule functions will be available via `path.any_function()`.

From the content of the `os.path` submodule, we select only some functions that are potentially useful to us.

The `basename(my_path)` function returns the last element of the `my_path` path name, ie if it is a file address, it returns the file name, if it is a folder, it returns the folder name:

```python
>>> os.path.basename("C:/my_folder/my_file.xls")
'my_file.xls'
>>> os.path.basename("C:/my_folder")
'my_folder'
```

The `dirname(my_path)` function returns the parent folder of the last path element:

```python
>>> os.path.dirname("C:/my_folder/my_file.xls")
'C:/my_folder'
>>> os.path.dirname("C:/my_file")
'C:/'
```

We often need to compose a path from its individual parts, eg `C:\main_folder`, `other_folder` and `filename.xls`, which we have stored separately in some variables. We can do this either manually:

```python
a = "C:/main_folder"
b = "next_folder"
c = "filename.xls"
path = a + "/" + b + "/" + c
path
"C:/main_folder/other_folder/filename.xls"
```

or in a slightly shorter and safer way with the `join` function from the `os.path` module:

```python
path = os.path.join(a, b, c)
path
"C:\\main_folder\\other_folder\\filename.xls"
```

To verify that the location (file or folder) exists, use the `exists` function:

```python
>>> os.path.exists("C:/my_folder/my_existing_file.xls")
True
>>> os.path.exists("C:/my_folder/a_nonexisting_file.txt")
False
```

Sometimes it's also useful to find out if a given location is a folder or file address:

```python
# Verifies that a path is a file path
>>> os.path.isfile("C:/my_folder/my_file.xls")
True
>>> os.path.isfile("C:/my_folder")
False

# Verifies if a path is a folder path
>>> os.path.isdir("C:/my_folder/my_file.xls")
False
>>> os.path.isdir("C:/my_folder")
True
```

> **Task 3.** Modify the solution of task 2 to use the function `os.path.join`.

## Split a string with a character

For the next part of this lesson, it will be useful to get familiar with one technique of working with text strings, which was not discussed in the lesson on data types. It is the division of a string by a given character or series of characters using the `split` method, which is a function that is called directly on a given string or on a variable containing a string:

```python
>>> "anaconda".split("a")
['', 'n', 'cond', '']
```

We see that the `split` function returns a list of individual parts of the original string, divided by the specified character. If this character is at the beginning resp. the end of the string, the resulting list contains an empty string at the beginning resp. the end.

If we use the `split` function without an argument, ie without specifying the string by which the input string is to be divided, it will be divided by all "empty characters", ie by a space, a tab (`\t` character) or a newline character (`\n` character). If the text contains a sequence of any blanks in a row, this sequence is interpreted as if it were one blank character (ie the string is split only once at this point):

```python
>>> text = "Probability is\tthe branch of mathematics\nconcerning numerical descriptions of how likely\nan event is to occur"
>>> print(text)
Probability is    the branch of mathematics
concerning numerical descriptions of how likely
an event is to occur

>>> text.split()
['Probability', 'is', 'the', 'branch', 'of', 'mathematics', 'concerning', 'numerical', 'descriptions', 'of', 'how', 'likely', 'an', 'event', 'is', 'to', 'occur']
```

In this way, you can easily divide a text into individual words.

## Reading text files

To illustrate, imagine a text file containing the following three lines of text:

```
Probability is the branch of mathematics concerning numerical descriptions of how likely an event is to occur, or how likely it is that a proposition is true.
The probability of an event is a number between 0 and 1, where, roughly speaking, 0 indicates impossibility of the event and 1 indicates certainty.
The higher the probability of an event, the more likely it is that the event will occur.
```

Suppose a file with this text is stored at `C:\Documents and Settings\user\Documents\probability.txt.`

To open a file for reading, use the built-in `open` function:
```python
>>> my_file = open(r"C:\Documents and Settings\user\Documents\probability.txt", "r")
```

The value of the second parameter `"r"` is derived from the English "read" and indicates that the file will be opened for reading.

If we want to read everything in the file at once, we use the `read()` function. The result is a single text string containing the entire text:

```python
>>> a = my_file.read()
>>> print(a)
Probability is the branch of mathematics concerning numerical descriptions of how likely an event is to occur, or how likely it is that a proposition is true.
The probability of an event is a number between 0 and 1, where, roughly speaking, 0 indicates impossibility of the event and 1 indicates certainty.
The higher the probability of an event, the more likely it is that the event will occur.
```
It is important to close the file after each action with it:

```python
>>> my_file.close()
```
Another option is to read only a single line using the `readline()` function (attention: in our text, the whole paragraph is a single line!). Repeated calls to this function read the individual lines one by one:

```python
>>> my_file = open(r"C:\Documents and Settings\user\Documents\probability.txt", "r")
>>> a = my_file.readline()
>>> b = my_file.readline()
>>> print(a)
Probability is the branch of mathematics concerning numerical descriptions of how likely an event is to occur, or how likely it is that a proposition is true.
>>> print (b)
The probability of an event is a number between 0 and 1, where, roughly speaking, 0 indicates impossibility of the event and 1 indicates certainty.
>>> my_file.close()
```

Finally, the last option is to read the entire text line by line using the `readlines()` function. In this case, the result is a list of text strings containing individual lines (note the `\n` characters at the end of each line):

```python
>>> my_file = open(r"C:\Documents and Settings\user\Documents\probability.txt", "r")
>>> a = my_file.readlines()
>>> print(a)
['Probability is the branch of mathematics concerning numerical descriptions of how likely an event is to occur, or how likely it is that a proposition is true.\n', 'The probability of an event is a number between 0 and 1, where, roughly speaking, 0 indicates impossibility of the event and 1 indicates certainty.\n', 'The higher the probability of an event, the more likely it is that the event will occur.']
>>> my_file.close ()
```
> **Task 4.** Save the text ("manually", eg using Notepad) to a text file. Then open the file in Python and find out the number of lines, the number of words and the number of characters in the text.

In applications, we often want to read from a file "line by line". E.g. it can be a data table in the format `.csv` ("comma-separated values​"), which is a simple text file with tabular data that can be opened in MS Excel. Reading "line by line" then means reading individual rows of the table. It is possible to use the already mentioned function `readlines`, which returns a list of lines - this can of course be followed by a `for` cycle:

```python
f = open("table.csv", "r")
lines = f.readlines()
f.close()
for l in lines:
    # There will be some action with variable l
```

However, the object returned by the `open` function can be directly passed through in the loop, so it behaves like a list of rows:

```python
f = open("table.csv", "r")
for l in f:
    # There will be some action with variable l
f.close ()
```

In this case, however, the browsing is done using a so-called **cursor**, which is reflected, among other things, in the fact that if we go through the whole file to the end, the cursor is at the end of the file and further browsing returns nothing:

```python
>>> f = open("text.txt", "r")
>>> for l in f: print(l)

first line
second line
...
last line
>>> for l in f: print(l)

>>> f.close ()
```

In order to browse the file again, we would need to reload the file by calling the `open` function again.

In addition, the method of reading the list of rows with the `readlines` method has the advantage that only selected rows can be browsed. An good example is skipping the first line when reading tabular data, as the first line of a table is usually a header:

```python
f = open("table.csv", "r")
lines = f.readlines()
f.close()
for l in lines[1:]:
    # There will be some action with variable l
```

Finally, let's show how to open files without having to think about closing them later. This is possible using a `with` clause, which creates an indented block of code. Once the code returns to the previous indentation level, the file closes automatically. The syntax is as follows:

```python
with open("some_file.txt") as f:
    f.readlines()
    ...
# The code continues here and the file is already closed
```

> **Task 5.** Open the table [precipitation_2014.csv](https://owncloud.cesnet.cz/index.php/s/SMwOA7a4evWXRhC) in MS Excel and explore what it contains. Then close it and open it in Notepad: what separates the individual columns? Write a Python program to open the table and calculate the average precipitation in August. (Note: data comes from CHMI.)

## Writing text files

Conversely, if we want to write to a text file, it is necessary to open it with an argument `"w"` (from "write"):

```python
my_file = open(r"C:\Documents and Settings\user\Documents\letter_to_grandpa.txt", "w")
```

The file that we open in this way may not actually exist at all and is created with this command (but the appropriate folder must exist). If the file already exists, all of its content is deleted and replaced with the new content.

Writing is done using the `write()` function. If you want to write a text with multiple lines, you must use the end-of-line character `\n`. Again, don't forget to close the file at the end.

```python
>>> my_file.write("Hello grandpa.\n")
>>> my_file.write("Don't you know\nwhat happened to grandma?")
>>> my_file.close()
```

If we read the resulting file, we get:

```python
>>> my_file = open(r"C:\Documents and Settings\user\Documents\letter_to_grandpa.txt.txt", "r")
>>> print(my_file.read())
Hello grandpa.
Don't you know
what happened to grandma?
>>> my_file.close()
```

It remains to be solved how to write to an existing file without overwriting it all when it is opened. This can be done by opening it with an `"a"` argument (from "append"). Then the `write()` function writes the given text to the end after the already existing text:

```python
>>> my_file = open(r"C:\Documents and Settings\user\Documents\letter_to_grandpa.txt", "a")
>>> my_file.write("\nI've heard some crazy stories...")
>>> my_file.close ()
```

The result looks like this:

```python
>>> my_file = open(r"C:\Documents and Settings\user\Documents\letter_to_grandpa.txt", "r")
>>> print(my_file.read())
Hello grandpa.
Don't you know
what happened to grandma?
I've heard some crazy stories...
>>> my_file.close()
```

> **Task 6.** Write a program that replaces decimal dots with decimal commas in the table [precipitation_2014.csv](https://owncloud.cesnet.cz/index.php/s/SMwOA7a4evWXRhC).

## Summary

## Tasks

1. Write a program that creates a reverse copy of a text file (ie the text in the output file will be mirrored).
2. Write a program that calculates the frequency of occurrence of a given letter in the specified input text file. Solve first using the `count` method of lists, then without this method.
3. In the folder [data_temperature](https://owncloud.cesnet.cz/index.php/s/C3cV43wNi3ngFiJ) you will find text files containing data on temperature measurement (in dozens of degrees Celsius) at individual European stations (each station corresponds to one file). Write a program that extracts temperature values ​​for May 1998 from these text files, calculates their average for each station ​​and saves the result in a new text table in the format `.csv` (the column separator will be a semicolon). The output table will contain two columns: "STAID" with the station identifier and "T" with the average temperature in May 1998.