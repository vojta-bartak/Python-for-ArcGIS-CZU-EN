# Lesson 6: Interactive program inputs and random numbers

In this lesson, you will learn how to interactively enter inputs into a program in Python, which we run on the console (eg in the IDLE environment). Inputs are entered using the `input` function. Because its properties are different in Python series 2.x and series 3.x, we will discuss both variants separately. Next you will learn how to generate random numbers in Python.

## `input` and `raw_input` functions in Python 2.x

In Python 2.x versions, there are two functions, `input` and `raw_input`.

The `input` function prints a text entered on the console and then waits for the user to enter input on the console:

```python
>>> input("Dear user, enter a number:")
Dear user, enter a number:
```

After typing a number and confirming with the `Enter` key, the function returns the value entered by the user, automatically evaluating which data type it is:

```python
>>> input("Dear user, enter a number:")
Dear user, enter a number: 5
5
```

In this case, the function automatically recognizes that it is a number because a number without quotation marks was entered. If we wanted the function to read the input as a text string, we would have to enter the input in quotation marks:

```python
>>> input("Dear user, enter a text:")
Dear user, enter a text: "5"
'5'
```

Other data types can be entered similarly:

```python
>>> input("Dear user, enter a list:")
Dear user, enter a list: [1,2,3,4]
[1, 2, 3, 4]
```

or eg a function call:

```python
>>> input("Dear user, enter a list from 0 to 5:")
Dear user, enter a list from 0 to 5: range(6)
[0, 1, 2, 3, 4, 5]
```

The `raw_input` function, on the other hand, returns any input as a text string:

```python
>>> raw_input("Dear user, enter a number:")
Dear user, enter a number: 5
'5'

>>> raw_input("Dear user, enter a list:")
Dear user, enter a list: [1,2,3,4]
'[1,2,3,4]'

>>> raw_input("Dear user, enter a list from 0 to 5:")
Dear user, enter a list from 0 to 5: range(6)
'range(6)'
```

## Use of console inputs into calculations

In the above examples, we only had the result of calling the `input` function written to the console. Usually, however, we want to perform some other calculations or operations with it. We ensure this by saving the result of `input` or `raw_input` in a variable:

```python
>>> a = input("Dear user, enter a number:")
Dear user, enter a number: 5
>>> a + 2
7
```

However, in the case of the `raw_input` function, we must not forget to convert the text input to the required data type:

```python
>>> a = raw_input("Dear user, enter a number:")
Dear user, enter a number: 5
>>> int(a) + 2
7
```

It is also possible to use the `eval` function, which takes a text input and tries to interpret it as a Python code and return the desired output:

```python
>>> my_list = raw_input("Dear user, enter list from 0 to 5:")
Dear user, enter a list from 0 to 5: range(6)
>>> my_list
'range(6)'
>>> eval(my_list)
[0, 1, 2, 3, 4, 5]
```

Therefore, the behavior of the `input()` function can be mimicked using `eval(raw_input())`:

```python
>>> list = eval (raw_input ("Dear user, enter list from 0 to 5:"))
Dear user, enter list from 0 to 5: range (6)
>>> list
[0, 1, 2, 3, 4, 5]
```
> **Task 1.** Write a program that prompts the user to enter a natural number and then returns its factorial.

> **Task 2.** Write a program that prompts the user to enter two numbers one by one and then tells if the larger one is divisible by the smaller one.

## `input` function in Python 3.x

The following changes have been made in Python 3.x:

- the `raw_input` function has been canceled,
- the behavior of the `input` function has been changed to the original behavior of the `raw_input` function.

This means that only the `input` function is used for interactive input via the console, and the input is always passed as a text string. If you want to work with it as a number, list, etc., you need to use casting (conversion function `int`, `float`, `list`, etc.), or the function `eval`.

## Generate random numbers

The `random` module in Python is used to generate random numbers, which is part of the basic equipment of the language. The module must first be loaded with the `import` command:

```python
>>> import random
```

The individual functions of the module are then accessed, as is usual in Python, via the module name, the dot, and the function name. E.g. the function `random()`, called without arguments, generates a random number from the interval (0, 1) (from the uniform distribution):

```python
>>> import random
>>> random.random()
0.6744697203253585
>>> random.random()
0.7169711430089877
>>> random.random()
0.4213975602144999
```

The module can be loaded and further used under a custom alias:

```python
>>> import random as rn
>>> a = rn.random()
>>> a
0.8591162717665027
```

The function `randint(a, b)` returns a random integer from the interval <`a`,`b`> (including both limits):

```python
>>> rn.randint(-100, 100)
70
>>> rn.randint(-100, 100)
-89
```

The `choice(seq)` function returns a randomly selected element from a sequence (list, tuple, etc.) `seq`:

```python
>>> my_list = [1, "two", 3, "four", 5]
>>> rn.choice(my_list)
5
>>> rn.choice(my_list)
'two'
```

The `sample(population, k)` function returns a random selection of the size `k` from the sequence `population`:

```python
>>> rn.sample(range(100), 10)
[10, 67, 93, 45, 56, 17, 71, 8, 91, 9]
```

The function `uniform(a, b)` returns a random number generated from a uniform distribution on the interval <`a`,`b`>. (Note: same as `a + random() * abs(a - b)`.)

```python
>>> rn.uniform(2,4)
2.8693870960257666
```

The `gauss(mu, sigma)` function returns a random number generated from a normal distribution with a mean of `mu` and a standard deviation of `sigma`:

```python
>>> rn.gauss(0, 1)
-0.072104281974643761
```

A real computer-based random number generator does not exist (and in principle cannot exist). The numbers that we call "random" are in fact only *pseudo-random*, ie those that only appear to be random. In fact, each additional number in a sequence of these "pseudo-random" numbers is precisely (and always in the same way) calculated from the previous number using a sophisticated algorithm. So why do we call (and use) them as they really were random? What is their "randomness"? It consists in the fact that if we generate an arbitrarily long sequence, it will always "look" random statistically. No statistical test reveals a correlation between successive numbers.

It follows that if we were to generate two separate sequences of random numbers with a given (same) generator, starting always from the same first number, both sequences would be identical (although each of them would appear random on its own). In practice, this problem is solved by starting with a different number each time, ann this first number is called the *seed*. By default, the seed is automatically derived from the instant system time of the computer.

However, it is also possible to set the seed to a specific fixed value, which is useful if, for example, we want to repeatedly test an algorithm working with random numbers, while we want the same values ​​to enter each test. Use the `seed` function to set the seed:

```python
>>> rn.seed(123)
>>> rn.random()
0.052363598850944326
>>> rn.random()
0.08718667752263232
>>> rn.random()
0.4072417636703983
>>> rn.seed(123)
>>> rn.random()
0.052363598850944326
>>> rn.random()
0.08718667752263232
>>> rn.random()
0.4072417636703983
```

As can be seen from the example, after setting the seed to the same value (in our case 123), the following sequence forms the same numbers.

> **Task 3.** Generate 1000 numbers from an even distribution on the interval(0, 1) and find out what percentage of them is greater than 0.7.

## Summary

## Tasks

1. Create a program that will test you in basic math, namely multiplication of two natural numbers. The program randomly generates an exercise and prompts you to enter a result. In case of a wrong answer, it will correct you; in case of a correct answer, it will congratulate you.
2. Modify the program from the previous task so that in case of a wrong answer it will force you to enter the result again, until you enter the correct one.
3. Modify the program from the previous task so that when the exercise succesfully ends, you will be asked if you want to continue with a next excercise. If you choose "yes" (eg by entering "Y" as "YES"), it will give you another exercise. If you select "no" (eg "N" as "NO"), it will end.
4. Generate 10,000 numbers from the normal distribution with a mean value of 13 and a standard deviation of 2.3. Calculate their sample mean and sample standard deviation. Calculate the same values ​​from a random selection of 100 numbers from the generated set of 10,000 numbers. Which sample values ​​are closer to the mean and standard deviation of the original normal distribution? Why?