import pytest

from python_toolbox.math_tools import (factorial, inverse_factorial, from_factoradic, to_factoradic)


class TestFactorial:
    @pytest.mark.parametrize("value, expected_factorial",
                             [(0, 1), (1, 1), (2, 2), (5, 120), (20, 2432902008176640000),
                              (100, 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000),
                              (-1, None), (-5, None), (-4.2, None), (4.2, None)])
    def test_factorial(self, value, expected_factorial):
        if expected_factorial is not None:
            assert factorial(value) == expected_factorial, f"{value}! should be {expected_factorial}"
        else:
            with pytest.raises(Exception):
                factorial(value)

    @pytest.mark.parametrize("value, round_up, expected_res",
                             [(0, True, 0), (0, False, 0), (1, True, 1), (1, False, 1), (2, True, 2), (2, False, 2),
                              (6, True, 3), (25, True, 5), (25, False, 4), (2432902008176639999, False, 19),
                              (2432902008176639999, True, 20), (2432902008176640001, False, 20),
                              (2432902008176640001, True, 21), (0.1, True, 1), (0.1, False, 0),
                              (6.214, True, 4), (6.214, False, 3), (-2, None, None), (-0.0001, None, None)])
    def test_inverse_factorial(self, value, round_up, expected_res):
        if expected_res is not None:
            assert inverse_factorial(value, round_up=round_up) == expected_res, \
                f"{value} is factorial (with round_up = {round_up}) of {expected_res}"
        else:
            with pytest.raises(AssertionError):
                inverse_factorial(value)

    def test_factorial_and_inverse(self):
        for number in range(1, 1000):
            assert inverse_factorial(factorial(number)) == number, f"Error in {number}"

    def test_from_to_factoradics(self):
        with pytest.raises(AssertionError):
            to_factoradic(-1)
        for number in range(1000):
            assert from_factoradic(to_factoradic(number)) == number, f"Error in {number}"


