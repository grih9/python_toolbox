# Copyright 2009-2017 Ram Rachum.
# This program is distributed under the MIT license.

import math
import collections
import itertools
import numbers

infinity = float('inf')
infinities = (infinity, -infinity)


def factorial(number, start=1):
    '''
    Calculate a factorial.

    This differs from the built-in `math.factorial` in that it allows a `start`
    argument. If one is given, the function returns `(x!)/(start!)`.

    Examples:

        >>> factorial(5)
        120
        >>> factorial(5, 3)
        60

    '''
    assert number >= 0
    from python_toolbox import misc_tools
    return misc_tools.general_product(range(start, number + 1), start=1)


def inverse_factorial(number, round_up=True):
    '''
    Get the integer that the factorial of would be `number`.

    If `number` isn't a factorial of an integer, the result will be rounded. By
    default it'll be rounded up, but you can specify `round_up=False` to have
    it be rounded down.

    Examples:

        >>> inverse_factorial(100)
        5
        >>> inverse_factorial(100, round_up=False)
        4

    '''
    assert number >= 0
    if number <= 1:
        if 0 < number < 1:
            return int(round_up)  # Heh.
        return number

    current_number = 1
    for multiplier in itertools.count(start=2):
        current_number *= multiplier
        if current_number == number:
            return multiplier
        if current_number > number:
            return multiplier if round_up else (multiplier - 1)
    return None


def from_factoradic(factoradic_number):
    '''
    Convert a factoradic representation to the number it's representing.

    Read about factoradic numbers here:
    https://en.wikipedia.org/wiki/Factorial_number_system

    Example:

        >>> from_factoradic((4, 0, 2, 0, 0))
        100

    '''
    from python_toolbox import sequence_tools
    assert isinstance(factoradic_number, collections.abc.Iterable)
    factoradic_number = sequence_tools.ensure_iterable_is_sequence(factoradic_number)
    number = 0
    for i, value in enumerate(reversed(factoradic_number)):
        assert 0 <= value <= i
        number += value * factorial(i)
    return number


def to_factoradic(number, n_digits_pad=0):
    '''
    Convert a number to factoradic representation (in a tuple.)

    Read about factoradic numbers here:
    https://en.wikipedia.org/wiki/Factorial_number_system

    Example:

        >>> to_factoradic(100)
        (4, 0, 2, 0, 0)


    Use `n_digits_pad` if you want to have the result padded with zeroes:

        >>> to_factoradic(100, n_digits_pad=7)
        (0, 0, 4, 0, 2, 0, 0)

    '''
    assert isinstance(number, numbers.Integral)
    assert number >= 0
    assert isinstance(n_digits_pad, numbers.Integral)
    n_digits = inverse_factorial(number, round_up=False) + 1
    digits = [None for _ in range(n_digits)]
    current_number = number
    for i in range(n_digits)[::-1]:
        unit = factorial(i)
        digits[n_digits - i - 1], current_number = divmod(current_number, unit)
    result = tuple(digits)
    if len(result) < n_digits_pad:
        return ((0,) * (n_digits_pad - len(result))) + result
    return result
