# -*- coding: utf-8 -*-
"""
This script provides command-line tool to calculate basic arithmetic operation(add, subtract,
multiplication, power, division, quotient and remainder) and fibonacci sequence.

created on 8/12/2024

@author: Aziz Azizi
"""

import unittest

from functions import (add, subtract, multiply, power, division, quotient, remain, fibonacci)
# (This script imports functions from `functions.py` for arithmetic and Fibonacci operations, including:
#- add
#- subtract
#- multiply
#- power
#- division
#- quotient
#- remain
#- fibonacci
while True:
    # Loop to ensure the input for X enters correctly, otherwise it will execute the line 76
    X = input("Select: a(Arith) or f(Fibonacci): ").lower()
    """input
    getting X from the user, .lower() is to lower the input from user and not having capital
    X (string, optional): a for arithmetic, f for fibonacci
    """
    if X == "a":
        while True:  # Loop to ensure valid number is entered for 'a'
            try:
                a = int(input("Enter your first number: "))
                break
            except ValueError:
                # used to be sure value of a is int(number)
                print("Invalid input. Please enter a valid number.")

        while True:  # Loop to ensure a valid number is entered for 'b'
            try:
                b = int(input("Enter your second number: "))
                break
            except ValueError:
                # used to be sure value of b is int(number)
                print("Invalid input. Please enter a valid number.")
        while True:
            # Loop to ensure a valid math operator is entered, if not valid it will execute line 57
            c = input(
                "Select your arithmetic operation (+, -, *, **, /, //, %): "
            ).strip()
            if c == "+":
                print(f"The result of {a} + {b} = {add(a, b)}")
                # Calls the add(a,b) function from functions.py file
                break
            elif c == "-":
                print(f"The result of {a} - {b} = {subtract(a, b)}")
                # Calls the subtract(a,b) function from functions.py file
                break
            elif c == "*":
                print(f"The result of {a} * {b} = {multiply(a, b)}")
                # Calls the multiply(a,b) function from functions.py file
                break
            elif c == "**":
                print(f"The result of {a} to the power of {b} = {power(a, b)}")
                # Calls the power(a,b)(a to the power of b) function from functions.py file
                break
            elif c == "/":
                print(f"The result of {a} / {b} = {division(a, b)}")
                # Calls the division(a,b)(also gives float(decimal) number) function from functions.py file

                break
            elif c == "//":
                print(f"The whole number of {a} // {b} = {quotient(a, b)}")
                # Calls the quotient(a,b)(returns the quotient) function from functions.py file
                break
            elif c == "%":
                print(f"The remainder of {a} % {b} = {remain(a, b)}")
                # Calls the remain(a,b)(gives the remainder) function from functions.py file
                break  # Exit the loop on valid input
            else:
                print(
                    "Invalid operation. Please select a valid operator (+, -, *, **, /, //, %)."
                )

        break  # Exit the loop after processing arithmetic operations user entered

    elif X == "f":
        while True:
            try:
                N = int(input("How many Fibonacci numbers do you want? "))
                # If input is valid, calculate the Fibonacci sequence
                fib_sequence = fibonacci(N)
                # Call the fibonacci function from functions.py to get the sequence
                print(f"The Fibonacci sequence of {N} is: {fib_sequence}")
                # f'' insert variables or expressions inside the curly braces{} directly within the string. new in py 3
                break  # Exit the loop on valid input
            except ValueError:
                # used to be sure value of N is int(number)
                print("Invalid input, please enter a valid number.")
        break  # Exit the loop after showing the Fibonacci sequence

    else:
        print(
            "Please select correctly. Please choose 'a' for arithmetic or 'f' for Fibonacci.")
