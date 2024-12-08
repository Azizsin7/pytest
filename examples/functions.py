# -*- coding: utf-8 -*-
"""
    Module name: Arithmetic.py
    @Author: Aziz Azizi
    created on 5/12/2024
"""

# Func Definition
def add(a, b):
    """ 
    Returns the sum of the numbers
    Examples:
    >>> add(2, 2)
    4
    >>> add(4, 2)
    6
    >>> add(-5, 5)
    0
    """
    return a + b

def subtract(a , b):
    """ 
    Returns the difference between two numbers
    Examples:
    >>> subtract(6, 2)
    4
    >>> subtract(6, 9)
    -3
    >>> subtract(8, 8)
    0
    """
    return a - b

def multiply(a , b):
    """
    Returns the multiplication of two numbers
    Examples:
    >>> multiply(6, 6)
    36
    >>> multiply(5, 3)
    15
    >>> multiply(1, 8)
    8
    """
    return a * b

def power(a ,b):
    """ 
    Returns the a to the power of b
    Examples:
    >>> power(2, 2)
    4
    >>> power(4, 3)
    64
    >>> power(6, 2)
    36
    """
    return a ** b

def division(a , b):
    """ 
    Returns divisions of two number, even decimal
    Examples:
    >>> division(4, 2)
    2.0
    >>> division(12, 4)
    3.0
    >>> division(7, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
    

def quotient(a , b):
    """ 
    Returns the quotient number of division
    Examples:
    >>> quotient(15, 5)
    3
    >>> quotient(16, 4)
    4
    >>> quotient(18, 3)
    6
    >>> quotient(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b

def remain(a , b):
    """ 
    Returns the remaining of division
    Examples:
    >>> remain(10, 3)
    1
    >>> remain(12, 4)
    0
    >>> remain(16, 5)
    1
    >>> remain(8, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a % b

def fibonacci(n, a=0, b=1):
    """ Returns the Fibonacci sequence up to n numbers.

    Args:
        n (int, optional): The total number of Fibonacci numbers to generate.
        a (int): The starting number of the sequence. Defaults to 0.
        b (int): The second number of the sequence. Defaults to 1.

    Returns:
        List: A list containing the Fibonacci sequence.
        
    Examples:
    >>> fibonacci(4)
    [0, 1, 1, 2]
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    >>> fibonacci(2)
    [0, 1]
    """
    fib_sequence = [a, b]
    while len(fib_sequence) < n:
        # Len() returns the number of items(n)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        # .append() add the new item end of the list
    return fib_sequence


def leap_year(year):
    """
    Determine whether a given year is a leap year or not.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    Examples:
    >>> leap_year(2000)
    True
    >>> leap_year(2020)
    True
    >>> leap_year(1994)
    False
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400
            else:
                return False  # Divisible by 100 but not 400
        else:
            return True  # Divisible by 4 but not 100
    return False  # Not divisible by 4


