Pytest
---
In this rep you can find the examples of pydoc, doctest and unitest.

---
First create a file **(functions.py)** then create another file and name it: **(test_functions.py)**

* **both files should be in the same folder(directory).**
* **save the file before runnig the command or making any changes.**
---

copy any of the functions you want:

1. add function (copy the below code to the functions.py)
```python
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
```

then run this command in terminal (ctrl+j):

>pydoc:
```terminal 
   python -m pydoc path/function.py
```

>doctest:

```terminal
    python -m doctest -v path/function.py

```


* add the below to the **(test_functions.py)**
  ```python
  import unittest
  from functions import (add)
  class TestFunctions(unittest.TestCase):
    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(4, 2), 6)
        self.assertEqual(add(-5, 5), 0)
  ```

  then run this command in terminal (ctrl+j):
  >unitest:
  ```bash
    python -m unittest path/test_function.py
   ```
---
2. subtract function (copy the below code to the functions.py)

```python
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
```

then run this command in terminal (ctrl+j):

>pydoc:
```terminal 
   python -m pydoc path/function.py
```

>doctest:

```terminal
    python -m doctest -v path/function.py
```

* add the below to the **(test_functions.py)**
>unitest
```python
    import unittest
    from functions import (subtract)
    class TestFunctions(unittest.TestCase):
        def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(subtract(6, 2), 4)
        self.assertEqual(subtract(6, 9), -3)
        self.assertEqual(subtract(8, 8), 0)
  ```
then run this command in terminal (ctrl+j):
  >unitest:
  ```bash
    python -m unittest path/test_function.py
   ```

---
3. multiply function (copy the below code to the functions.py)
```python
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
```
then run this command in terminal (ctrl+j):

>pydoc:
```terminal 
   python -m pydoc path/function.py
```

>doctest:

```terminal
    python -m doctest -v path/function.py
```


* copy the below code to the **(test_functions.py)**
```python
    import unittest
    from functions import (multiply)
    class TestFunctions(unittest.TestCase):
        def tes_multiply(self):
        """Test the multiply function."""
        self.assertEqual(multiply(6, 6), 36)
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(1, 8), 8)
  ```
then run this command in terminal (ctrl+j):
  >unitest:
  ```bash
    python -m unittest path/test_function.py
   ```

---

4. power function (copy the below code to the functions.py)
```python
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
```

then run this command in terminal (ctrl+j):
>pydoc
```terminal 
   python -m pydoc path/function.py
```

>doctest:

```terminal
    python -m doctest -v path/function.py
```


* copy the below code to the **(test_functions.py)**
```python
    import unittest
    from functions import (power)
    class TestFunctions(unittest.TestCase):
        def test_power(self):
        """Test the power function."""
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(4, 3), 64)
        self.assertEqual(power(6, 2), 36)
  ```
then run this command in terminal (ctrl+j):
  >unitest:
  ```bash
    python -m unittest path/test_function.py
   ```

---

5. division function (copy the below code to the functions.py)
```python
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
```

then run this command in terminal (ctrl+j):
>pydoc
```terminal 
   python -m pydoc path/function.py
```

>doctest:

```terminal
    python -m doctest -v path/function.py
```

* copy the below code to the **(test_functions.py)**
```python
    import unittest
    from functions import (division)
    class TestFunctions(unittest.TestCase):
        def tes_division(self):
            """Test the division function."""
            self.assertEqual(division(4, 2), 2.0)
            self.assertEqual(division(12, 4), 3.0)
            with self.assertRaises(ValueError):
                division(7, 0)
  ```
then run this command in terminal (ctrl+j):
  >unitest:
  ```bash
    python -m unittest path/test_function.py
   ```

---

6. division function (copy the below code to the functions.py)
```python
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
```

then run this command in terminal (ctrl+j):
>pydoc
```terminal 
   python -m pydoc path/function.py
```

>doctest:

```terminal
    python -m doctest -v path/function.py
```

* copy the below code to the **(test_functions.py)**
```python
    import unittest
    from functions import (fibonacci)
    class TestFunctions(unittest.TestCase):
        def test_fibonacci(self):
            """Test the fibonacci function."""
            self.assertEqual(fibonacci(4), [0, 1, 1, 2])
            self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
            self.assertEqual(fibonacci(2), [0, 1])
  ```
then run this command in terminal (ctrl+j):
  >unitest:
  ```bash
    python -m unittest path/test_function.py
   ```

---

7. leap_year function (copy the below code to the functions.py)
```python
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
```

then run this command in terminal (ctrl+j):
>pydoc
```terminal 
   python -m pydoc path/function.py
```

>doctest:

```terminal
    python -m doctest -v path/function.py
```

* copy the below code to the **(test_functions.py)**
```python
    import unittest
    from functions import (leap_year)
    class TestFunctions(unittest.TestCase):
        def test_leap_year(self):
            """Test the leap_year function."""
            self.assertEqual(leap_year(2000), True)
            self.assertEqual(leap_year(2020), True)
            self.assertEqual(leap_year(1994), False)
  ```
then run this command in terminal (ctrl+j):
  >unitest:
  ```bash
    python -m unittest path/test_function.py
   ```