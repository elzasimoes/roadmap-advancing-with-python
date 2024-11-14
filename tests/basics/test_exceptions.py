import sys
from io import StringIO

import pytest

from basics.exceptions.example import divide


class TestDivide:
    # Divides two positive numbers and returns the correct result
    def test_divide_two_positive_numbers(self):
        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        divide(6, 3)

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if the output is as expected
        assert 'Your answer is 2.0' in captured_output.getvalue()

    # Handles division by zero by catching ZeroDivisionError
    def test_handle_zero_division_error(self):

        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        divide(6, 0)

        # Reset redirect.
        sys.stdout = sys.__stdout__

        # Check if the output is as expected
        assert (
            'Please change `y` argument to non-zero value'
            in captured_output.getvalue()
        )

    def test_handle_string_division_error(self):

        # Capture the output
        captured_output = StringIO()
        sys.stdout = captured_output

        divide('x', 'y')

        sys.stdout = sys.__stdout__

        assert (
            'Both `x` and `y` must be numbers'
            in captured_output.getvalue()
        )
