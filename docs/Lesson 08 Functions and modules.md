# Lesson 8: Functions and modules

## Defining and calling a function

Often there is a situation where we want to use some part of our code repeatedly. For example, we may want to repeatedly count the factorial of a number in our program (and this number may be different each time). We have shown the calculation of the factorial in the chapter on the `for` cycle, the solution may look like this:

```python
factorial = 1
for i in range(n): factorial = factorial * (i + 1)
print(factorial)
```

The "most primitive" option would be to insert this code wherever we need to count the factorial in the code, of course always with the properly changed value of `n`.

The problem with such a solution arises when we want to change the factorial calculation itself - for example, if we find that we have made a mistake in the original code and it needs to be fixed. If we have the above code in our program in many places, it is necessary to rewrite it (correctly) in each such place. This is very inconvenient and, in addition, we easily make mistakes.

A more elegant solution is to create (ie define) a **function** that will perform the factorial calculation, and then call this function at the appropriate places.

The structure of a function definition is as follows:

```python
def function_name(parameter1, parameter2, ..., parameterN):
    body of the function
```

The definition is introduced by the keyword `def`, according to which the interpreter recognizes that it is a definition of a function. This is followed by a name, under which the function will be called. Then, a sequence of so-called **parameters** is defined in parentheses. Parameters are variables representing the values ​​entering the calculation that the function is to perform. **The body of a function** then contains statements (written on separate lines indented one level after the word `def`) that usually do something with the parameters. Let's show the function on a specific example of factorial calculation:

```python
def factorial(n):
    fact = 1
    for i in range (n): fact = fact * (i + 1)
    return fact
```

The `return` keyword terminates the function definition (but is not required, as we will see below), and specifies what value the function should return when the function is called.

If we send the code with the function definition to the compiler (or interpreter), it will not execute the commands in the function body, but instead it will store the function in the operational memory so that it can be called **at any time**. The function call has a structure analogous to its definition:

```python
function_name(argmunet1, argument2, ..., argumentN)
```

The individual arguments correspond exactly to the individual parameters of the function, they are actually specific values ​​that are substituted for the individual parameters when calling the function. Let's call our factorial function in the Python Shell console:

```python
>>> factorial(3)
6
>>> factorial(6)
720
>>> factorial(10)
3628800
```

The advantage of this solution is obvious: we can now use the `factorial` function with any integer argument in any place of our code, and if we want to change the function in some way, we only need to do so once, in its very definition.

Here is an example of a function with more than one parameter, such as a function that computes a given integer power of a given number:

```python
def power(x, y):
    result = 1
    for i in range(y): result = result * x
    return result
```

(Of course, we could have defined the function more easily: `def power(x, y): return x ** y`. However, examine the more complex definition above and realize that it will work for an integer power.)

When calling a function, it is necessary to write its arguments in the same order in which the corresponding parameters are defined:

```python
>>> power(3,4)
81
>>> power(4,3)
64
```

If, for some reason, we would like to enter the arguments in a different order than is defined by the parameters, it is possible to explicitly use the names of the corresponding parameters and the `=` operator when calling the function:

```python
>>> power(y = 4, x = 3)
81
```

Entering an argument using the parameter's name is useful for functions with a large number of parameters: it would be impractical to remember their order.

Parameters can have a so-called **default value**, so it is not necessary to enter them when calling the function. If no argument is specified, this default value is used. However, parameters with a default value must be placed at the end of the function definition, ie after parameters without default values. This is to ensure that parameters without default values ​​can be entered ​​based on parameters order.

Let's show the definition with a default parameter value on the example of the power function. If we define the default value of the `y` parameter as 2, the function will calculate squares when entering only one argument:

```python
def power(x, y = 2):
    result = 1
    for i in range(y): result = result * x
    return result
```

After calling the function in the Python Shell:

```python
>>> power(4) # The default value of the y parameter will be used here
16
>>> power(4, 3) # The user-specified value of the y parameter will be used here
64
```

Of course, the result of a function call can be stored in a variable, as you know it when using Python's built-in functions (eg `input`, `range`, `int`, etc.):

```python
>>> a = power(4)
>>> print(a)
16
```

Likewise, the arguments of a function can be entered directly using values ​​(see examples above), or using variables:

```python
>>> a = 4
>>> b = 5
>>> power(a, b)
1024
```

As already mentioned, functions may or may not have a return value. If a function only does something but does not return anything, it is sometimes called a *procedure*. It is recognized by the fact that it does not contain the keyword `return` in the definition. An example is a function that writes the result of a calculation to a text file:

```python
# A function that opens a text file and creates a new one, with mirror-inverted text
def invert_text(txt_in, txt_out):
    
    # read the input text file
    in_file = open(txt_in, "r")
    in_text = in_file.read()
    in_file.close()
    
    # write an output file with mirrored text
    out_file = open(txt_out, "w")
    for i in range(len(in_text), 0, -1):
        out_file.write(in_text[i-1])
    out_file.close()
```

If we store the call of such a function (procedure) in a variable, this variable will contain nothing (it will refer to the `None` object). Nevertheless, the function (procedure) does its job.

> **Task 1.** Write a function to calculate the *n*'th member of the Fibonacci sequence.

> **Task 2.** Write a function that opens a given text file and returns the number of its words (the parameter of the function will be a text string with the file address).

## Namespaces and their hierarchy

If we enter arguments of a function using variables, the question is whether this variable can be changed inside the function so that the change is reflected outside the function. Let's try it with the example of a function that only changes the value of an input variable:

```python
def change_value(s):
    a = a + 1
```

Let's check whether the function affects the original variable entered in it as an argument or not:

```python
>>> a = 5
>>> change_value(a)
>>> a
5
```

As you can see, the function does not affect the original variable. Why? This is because the `a = a + 1` statement in the body of the function actually creates a new variable `a`, the value of which is set using the `a` parameter (on the right side of the expression). However, this new variable is "visible" only within the function, as it is in its **namespace**.

A namespace is a kind of virtual space in which various *names* are defined, typically the names of variables and functions. There can be multiple namespaces, and they are arranged hierarchically. The basic namespace is the so-called *built-in namespace*, which contains, for example, the names of built-in functions such as `range` or `print`. Because these names are defined in the built-in namespace, they are available in any part of the Python code.

Another namespace, which is one hierarchical level lower, is the so-called *global namespace*. This is created automatically when you open the Python Shell console (or when you run a script). If we open the console by running the IDLE program from the program menu, or restart it with *Shell -> Restart Shell*, the global namespace is set to empty. Whenever a variable or function is created, the name is then added to the global space, so we can continue to work with it in that space. However, restarting the console empties the global namespace again:

```python
>>> a = 5 # Create a variable in the global namespace
>>> a # Variable exists ...
5
>>>
============================== RESTART: Shell =============== ===============
>>> a # After restarting the console, the variable in the global namespace is no longer available:

Traceback (most recent call last):
  File "<pyshell # 2>", line 1, in <module>
    and
NameError: name 'a' is not defined
```

In addition to the global namespace, we can create any number of mutually hierarchically nested so-called *local namespaces* within the script. Any name created in a given local space exists (ie is "available" or "visible") only within that namespace.

The local namespace is always created automatically within a body of a function. Therefore, if we create a variable `a` in a body of a function, we can treat this variable inside the body of this function, but not outside it:

```python
>>> def some_function(parameter): a = parameter + 1

>>> some_functions(5)
>>> a

Traceback (most recent call last):
  File "<pyshell # 4>", line 1, in <module>
    and
NameError: name 'a' is not defined
```

When evaluating the names used in the code, the lowest hierarchical level namespace is searched first. If the given name is not found here, the interpret proceeds to the next higher hierarchy of the namespaces.

