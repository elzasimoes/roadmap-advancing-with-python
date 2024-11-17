from pdb import post_mortem
from sys import exc_info

"""This code demonstrates a basic try-except block in
Python to handle exceptions.
It attempts to divide 1 by 0, which raises a ZeroDivisionError,
and then catches and handles this specific exception
by printing an error message."""

try:
    print(1 / 0)
except ZeroDivisionError:
    print('You cannot divide a value with zero')
except Exception:
    print('Something else went wrong')


"""
Attempts to open and read the contents of 'data.csv'. 
If the file is not found,
catches the FileNotFoundError and prints an
error message along with an explanation.
"""

try:
    with open('data.csv', encoding='utf-8') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
    print("Explanation: We cannot load the 'data.csv' file")

"""
Attempts to divide 1 by 3 and assigns the result to 'result'.
If a ZeroDivisionError
occurs, it catches the exception and prints the error message.
If no exception occurs,
it prints the result.
"""

try:
    result = 1 / 3
except ZeroDivisionError:
    errors = exc_info()
    print(errors)
    post_mortem(errors[2])
else:
    print(f'Your answer is {result}')


def divide(x, y):
    """
    Divides two numbers, `x` and `y`, and handles exceptions.

    Attempts to divide `x` by `y` and prints the result. If `y` is zero,
    catches a ZeroDivisionError and prompts to change `y` to a non-zero value.
    If either `x` or `y` is not a number, catches a TypeError and prompts
    to ensure both are numbers. Always prints a signature message at the end.
    """
    try:
        result = x / y
    except ZeroDivisionError:
        print('Please change `y` argument to non-zero value')
    except TypeError:
        print('Both `x` and `y` must be numbers')

    else:
        print(f'Your answer is {result}')
    finally:
        print('# Execute with error or not')
