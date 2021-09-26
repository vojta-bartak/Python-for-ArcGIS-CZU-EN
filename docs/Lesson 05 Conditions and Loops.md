# Lesson 5: Program control structures - loops and conditions

Program control structures (or just control structures) are language syntactic structures that allow conditional and repetitive execution of a sequence of commands.

## Logical expressions

A *logical expression* (or *logical statement*) is any statement to which a logical value (true/false) can be unambiguously attributed, ie to determine whether it is true or false. Assigning a logical value to a given expression is called its *evaluation*. Logical expressions are used in programming wherever a command (or series of commands) needs to be executed only if a certain condition is met (such commands are called *conditional statements*). The condition then takes the form of a logical expression, while its fulfillment/non-fulfillment is given by the logical value of the expression.

By comparing two values, it is possible to create a simple logical expression:

```python
>>> 3 < 5
True
>>> 3 > 5
False
```

You can also compare text strings. The comparison is then based on alphabetical order (ie on the so-called *lexicographic ordering*), with uppercase letters having priority over lowercase ones:

```python
>>> "hello" < "world"
True
>>> "Hello" < "HELLO"
False
```

Equality is tested by the `==` operator (be careful not to confuse it with the `=` operation, which assigns a value to a variable!):

```python
>>> a = 5
>>> a == 5
True
```

The inequality is tested with either `!=` or `<>` operator:

```python
>>> a != 5
False
>>> a <> 3
True
```

The `is` comparison operator is a bit more complicated. For numbers and strings, it tests equality in the same way as `==`, but for more complex objects, such as lists, it tests the identity of the objects (ie, whether they are the same object with the same address in memory):

```python
>>> a = 3
>>> b = 3
>>> a is b
True
>>> a = [1,2,3]
>>> b = [1,2,3]
>>> a is b
False
>>> a = b
>>> a is b
True
```

The opposite of `is` is the `is not` operator.

The `in` operator tests whether a certain element is in a given list or a certain character in a given string:

```python
>>> a = [1,2,3]
>>> 2 in a
True
>>> "o" in "hello"
True
```

Its opposite is `not in`:

```python
>>> a = [1,2,3]
>>> 4 not in a
True
>>> "z" not in "hello"
True
```

Compound logical statements can be created from simple ones using the so-called *logical operators* `and`, `or` and `not` (we are talking about so-called *logical operations* with logical expressions). The meaning of these operators is generally known from basic courses on logic, so we will limit the interpretation to a small example. E.g. if we want to test whether a value of a numeric variable is contained in a certain list *and at the same time* whether it is greater than 3, this can be done using the `and` operator:

```python
>>> mylist = [1,2,3,4]
>>> a = 4
>>> a in mylist and a > 3
True
```

The structure of a compound expression can be arbitrarily complex, containing any number of partial simple and complex expressions. If subexpressions are also compound, the priority of operations can be controlled using parentheses:

```python
>>> a in mylist and (a > 3 or a < -3)
True
```

The use of parentheses is governed by the known priority of operations: `not` is always evaluated first, then `and`, then `or`. If we omitted the parentheses in the last example, the meaning of the expression would change (answer: how?).

> **Task 1.** Enter the following command: `s = [1, 4, -10, 6, 13, -2]`. Decide in advance about the following expressions, whether they are true or false. Then verify:
>
> `s[1] < s[3] or 3 in s and len(s) == s[3]`
>
> `s[1] < s[3] or (3 in s and len(s) == s[3])`
>
> `(s[1] < s[3] or 3 in s) and len(s) == s[3]`
>
> `s[1] > s[3] and 3 not in s or len(s) == s[3]`
>
> `s[1] > s[3] and (3 not in s or len(s) == s[3])`
>
> `(s[1] > s[3] and 3 not in s) or len(s) == s[3]`
>
> `s[1] > s[3] and not (3 not in s or len(s) == s[3])`
>
> `not (s[1] > s[3] and 3 not in s) or len(s) == s[3]`
>
> `s`

## Conditional statements

A statement or command is called *conditional* if its execution only happens if a certain condition is met. The condition can be any logical expression, and the fulfillment of the condition is given by its logical value. The syntax of conditional statements in Python is very intuitive, as it copies the syntax of the common language: *if* the condition is met, execute the following command(s):

```python
if condition: command
```

In case of multiple commands:

```python
if condition:
    command 1
    command 2
    command 3
    ...
```

Here we see the block structure of code based on mandatory indentation, something typical and specific for Python langauage. Complying statements are indented one level (= four spaces) to the right of the line with the keyword `if`. Any statement indented to the level of the word `if` will no longer be related to the condition, ie it will be executed regardless of its fulfillment or non-fulfillment.

Let's give an example:

```python
>>> a = 5
>>> b = 6
>>> if a < 6: print a
    
5
>>> if b < 6: print b
    
>>> if a < b:
    print a
    print b
    print a, "is less than", b

5
6
5 is less than 6
```

> When writing a conditional statement to the Python Shell window, one needs to press the `Enter` key twice to execute the code. By pressing the `Enter` key a second time, we tell the interpreter that we have finished writing and the whole block can be interpreted (ie executed). This is why there is always one blank line after the last line of the notation.

In addition to specifying what commands to execute if a condition is met, you can also tell the program what commands to execute if the condition is not met. The syntax is intuitive again: *if* the condition applies, execute the following command(s), *else* (meaning "otherwise") execute alternative command(s):

```python
if condition:
    command 1
    command 2
else:
    command 3
    command 4
```

This time we show an example in the form of a script:

```python
a = 5
b = 6
if a == b:
    print(str(a) + " equals " + str(b))
else:
    print(str(a) + " does not equal " + str(b))
```

After running the script, the Python Shell console returns:

```python
5 does not equal 6
```

It is also often the case that we need to gradually test several different conditions, under each of which corresponding commands should be executed. The structure of the notation is: *if* condition 1 applies, execute command(s) 1, *else if* condition 2 applies, execute command(s) 2, *else* execute command(s) 3. There can be any number of conditions chained in this way, optionally with the final *else* section at the end, followed by statements executed if none of the previous conditions are met.

One way to implement the scheme described above is as follows:

```python
a = 5
b = 6
if a == b:
    print a, " equals ", b
else:
    if a < b:
        print a, " is less than ", b
    else:
        print a, " is greater than ", b
```

As can be seen, when concatenating the conditions this way, each further condition is indeted one level deeper. If there is more than few conditions this might result in an unclear and not very nice code. Fortunately, there is an alternative notation in Python that uses the `elif` keyword, which is actually an abbreviation of `else if`. The usage is evident from the following example (again, the sequence `if`-`elif`-`elif`-...-`elif` may or may not end with the `else` part):

```python
a = 5
b = 6
if a == b:
    print a, " is equal ", b
elif a < b:
    print a, " is less than ", b
else:
    print a, " is greater than ", b
```

> **Task 2.** Write a script that decides for given two numbers whether the larger one is divisible by the smaller one.

## The `while` loop

Sometimes we need to execute a command or series of commands repeatedly until a certain condition is occurs (or, conversely, expires). The *while* loop is used for this. In Python, its syntax is as follows:

```python
while condition:
    command 1
    command 2
    ...
    command n
```

As long as the condition is valid, the sequence of commands 1, 2, ..., n will be executed repeatedly. It is important that within these commands sooner or later something happens so that the condition no longer applies. Otherwise, a so-called *infinite loop* would arise. We would then have to forcibly interrupt the program with the keyboard shortcut `Ctrl` + `C`, or as a last resort, use the Windows Task Manager to terminate the task.

An example of using the `while` loop is calculation of the factorial of a given natural number, for example 20:

```python
n = 20
fact = 1
i = 2
while i <= n:
    fact = fact * i
i = i + 1
print(fact)
```

The condition for the continuation of the loop is the validity of the statement `i <= n`. This statement will certainly cease to be valid once, because in each step the value of the variable `i` is increased by one unit, so that once it will definitely exceed the value of `n`. Once this happens, the loop will no longer be executed and the program will continue executing statements (if there are any) written after the loop, ie indented to the level of the word `while`. In our case, it prints the result to the Python Shell console:

```python
2432902008176640000
```

Of course, for different values ​​of the variable `n` we get different results of the factorial.

The `while` loop can actually be considered a special kind of conditional statement, because it determines what the program should do if a condition is met. It can even be combined with the `else` clause, followed by a sequence of statements to be executed if the condition is no longer met (ie after the end of the loop):

```python
while condition:
    commands 1 to n
else:
    commands n + 1 to m
```

It can be argued that the program will behave in the same way if we write the commands n + 1 to m after the loop to the level of the word `while` instead of into the `else` section. This is true and the use of `else` in the `while` loop is actually very rare. However, this option is not entirely without purpose, as we will see later when we explore the `break` and `continue` commands.

> **Task 3.** Create a list with a Fibonacci sequence of length 100 using a `while` loop.

## The `for` loop

We use the `for` loop wherever we want to iterate over a list and do something with each of its items. The syntax is as follows:

```python
for item in list:
    command 1 (in which the variable item can be used)
    command 2 (in which the variable item can be used)
    ...
```

E.g. we can easily print individual items of the list:

```python
mylist = [0, "one", 2, "three", 4, "five"]
for i in mylist:
    print (i)
```

The result is:

```python
0
one
2
three
4
five
```

The same task could be solved using a `while` loop:

```python
i = 0
while i < len(mylist):
    print mylist[i]
    i = i + 1
```

The `for` cycle can be used wherever we know in advance how long our loop will be (ie how many iteration it will have). If, for example, we want to repeat a sequence of commands 20 times, it is enough to make a list of a given length and go through it using the `for` cycle. We do not have to use the items of the browsed list in individual commands at all:

```python
for i in [1]*20:
    print ("I won't interrupt the class with a loud croacking.")
```

When executed, it returns:

```python
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
I won't interrupt the class with a loud croacking.
```

It is often useful to iterate over a list of integer numbers from one to *n* (for example up to twenty). The `range` function can be useful for this:

```python
>>> range(20) # Returns a list of length 20, starting with zero
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

>>> range(5, 10) # Returns a list from 5 to 9
[5, 6, 7, 8, 9]

>>> range(5, 50, 3) # Returns a list from 5 to 49 with step of 3
[5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47]

>>> range(50, 5, -3) # Returns a list from 50 to 6 with step of -3
[50, 47, 44, 41, 38, 35, 32, 29, 26, 23, 20, 17, 14, 11, 8]
```

The above calculation of the factorial could therefore also look like this:

```python
n = 20
fact = 1
for i in range(n):
    fact = fact * i
print(fact)
```

The `for` loop can also be enclosed in square brackets to create a list. The following code creates a list of squares of numbers from 1 to 10:

```python
>>> a = [x**2 for x in range(1,11)]
>>> a
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

Of course, we could create the same list less briefly:

```python
>>> a = []
>>> for x in range(1,11): a.append(x**2)
>>> a
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

The first method is obviously more elegant and so it is more often used by experienced programmers.

> **Task 4.** Create a list with a Fibonacci sequence of length 100 using the `for` loop.

## The `break` and` continue` commands

The `break` and `continue` commands are used to interrupt a loop if there is a reason to do so. Therefore, they are typically used as part of a conditional statement, as can be seen from the following schematic representation of the syntax of the `break` command (we state both the version with the `while` and with the `for` loop):

```python
# Version with the while loop:
while condition 1:
    the first series of commands
    if condition2:
        second series of commands
        break
    else:
        the third series of commands
else:
    fourth series of commands
fifth series of commands

# Version with the for loop:
for item in list:
    the first series of commands
    if condition 2:
        second series of commands
        break
    else:
        the third series of commands
else:
    fourth series of commands
fifth series of commands
`` `

Note that the first `else` refers to the `if` statement, while the second `else` refers to the `while` or `for` loop.

The `break` statement causes an immediate break in the loop, and if there is (which may not!) also an `else` part related to the cycle, the program continues after it. In our schematic example, this means that as soon as in some step (iteration) of the loop the condition 2 applies, ie the command `break` is executed, the program automatically interrupts the cycle and continues by executing the fifth series of commands. On the other hand, if the condition 2 is never met during the loop, then after the loop the program continues with the fourth series of commands.

An example of using the `break` command with the `for` loop can be a script looking for a specific item (eg number 20) in a list:

```python
for number in mylist:
    if number == 20:
        print ("I just found number 20!")
        break
    else: 
        print("Number 20 is not in the list!")
```

The `continue` statement causes only the currently running iteration to be interrupted, and the program continues with the next step (iteration), skipping thus all the commands in the loop that are after the `continue` statement. It is used less often than the `break` command, because in most cases its use can be replaced by a suitably chosen conditional command. For this reason, we don't provide an example.

## Summary

## Tasks

1. From the sequence created by solving task 3 resp. 4, create a list containing only members divisible by three and determine its length.
2. Write a script that for given two lists of lengths *m* and *n*, where *m* > *n*, creates a new list, the first *n* elements of which will be formed by the elements of the shorter of the two lists, the rest of the list will be completed with elements of the longer of the two lists. Create a solution that works when you enter any two lists in any order.
3. Write a script to compare two numeric lists "item by item". The entry into the program will be any two lists and the type of comparison ("greater than", "less than" or "equals"). The output will be a list of the length of the shorter of the two lists, which on the index *i* will contain the result of the comparison (`True`/`False`) of the respective items of the input lists. E.g. for lists `a = [1,2,3]` and `b = [1,-2,4,5]` the "greater than" comparison will result in a list `[False, True, False]`.
4. Write a script that decides whether given two numbers have a common divisor.