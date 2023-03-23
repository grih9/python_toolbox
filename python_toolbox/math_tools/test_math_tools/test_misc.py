import math

import pytest

from python_toolbox.math_tools import binomial, convert_to_base_in_tuple, get_sign, cute_round, RoundMode, is_integer, \
    restrict_number_to_range, product, cute_floor_div, cute_divmod


class TestMisc:

    @pytest.mark.parametrize("big, small, res", [(7, 3, 35), (0, 0, 1), (1, 0, 1), (0, 1, 0),
                                                 (-1, -5, None), (235235, -1, None), (-235235, 1, None),
                                                 (1543, 634, 127103521979248139661884595050302692072114625333816461647571438364482801578062268185939019831927710543644891679108093639691467979466411177318250931548804667267192030646116875003881007119966764992383016174407823444352165249728639847571592229832113238415348489512831060701471487834812550521403788703534654431344329462541634971732197170414906629071055802381322184009159362499960475076746698583466181504060523973736761406471112019069930703149760846502951040)])
    def test_binomial(self, big, small, res):
        if res is None:
            with pytest.raises(AssertionError):
                binomial(big, small)
        else:
            assert binomial(big, small) == res

    @pytest.mark.parametrize("big", [2, 3, 6, 15, 55, 143, 10232])
    def test_binomial_ident(self, big):
        for small in range(big // 2 + 1):
            assert binomial(big, small) == binomial(big, big - small), f"big= {big}, small = {small}"

    @pytest.mark.parametrize("number", [0, 1, 5, 124, 1242145])
    def test_convert_to_base_tuple_trivial(self, number):
        for base in range(int(number) + 2, int(number) + 200, 4):
            assert convert_to_base_in_tuple(number, base) == tuple([number]), f"Error in number {number}, base {base}"

    @pytest.mark.parametrize("number", [-1, -5, -124214214])
    def test_convert_to_base_tuple_negative(self, number):
        with pytest.raises(NotImplementedError):
            convert_to_base_in_tuple(number, 2)

    @pytest.mark.parametrize("number", [-1.8, 1.8, 0.124214214, 0.99999999999999999999999999999999999999999, 0.000000000000000000000000000000000000000000000000000000000000000000000000000000001])
    def test_convert_to_base_tuple_float(self, number):
        with pytest.raises(AssertionError):
            convert_to_base_in_tuple(number, 2)

    @pytest.mark.parametrize("number, base, result", [(51346616, 16, (3, 0, 15, 7, 12, 11, 8)),
                                                      (2341263462323, 2,
                                                       (1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1))])
    def test_convert_to_base_tuple(self, number, base, result):
        assert convert_to_base_in_tuple(number, base) == result, f"Error in number {number}, base {base}"

    @pytest.mark.parametrize("number, sign", [(0, 0), (1, 1), (-1, -1), (0.000000000001, 1), (-0.000000001, -1),
                                              (325415125, 1), (-235235235235, -1), (-153523523.235235235235, -1),
                                              (1242142154263362372347.2464326234657854734, 1), (float('inf'), 1),
                                              (float('-inf'), -1)])
    def test_get_sign(self, number, sign):
        assert get_sign(number) == sign, f"Error in number {number}"

    @pytest.mark.parametrize("value, step, result", [(7.456, 1, 7), (7.654, 1, 8), (7.5, 1, 7),
                                                     (7.456, 0.1, 7.5), (7.456, 0.2, 7.4), (7.456, 0.01, 7.46)])
    def test_cute_round_closest_or_down(self, value, step, result):
        assert result - 10 ** (-10) < cute_round(value, round_mode=RoundMode.CLOSEST_OR_DOWN, step=step) < result + 10 ** (-10), \
            f"Error with value {value}, step {step}"

    @pytest.mark.parametrize("value, step, result", [(7.456, 1, 7), (7.654, 1, 8), (7.5, 1, 8),
                                                     (7.456, 0.1, 7.5), (7.456, 0.2, 7.4), (7.456, 0.01, 7.46)])
    def test_cute_round_closest_or_up(self, value, step, result):
        assert result - 10 ** (-10) < cute_round(value, round_mode=RoundMode.CLOSEST_OR_UP, step=step) < result + 10 ** (-10), \
            f"Error with value {value}, step {step}"

    @pytest.mark.parametrize("value, step, result", [(7.456, 1, 8), (7.654, 1, 8), (7.5, 1, 8),
                                                     (7.456, 0.1, 7.5), (7.456, 0.2, 7.6), (7.456, 0.01, 7.46)])
    def test_cute_round_always_up(self, value, step, result):
        assert result - 10 ** (-10) < cute_round(value, round_mode=RoundMode.ALWAYS_UP, step=step) < result + 10 ** (-10), \
            f"Error with value {value}, step {step}"

    @pytest.mark.parametrize("value, step, result", [(7.456, 1, 7), (7.654, 1, 7), (7.5, 1, 7),
                                                     (7.456, 0.1, 7.4), (7.456, 0.2, 7.4), (7.456, 0.01, 7.45)])
    def test_cute_round_always_down(self, value, step, result):
        assert result - 10 ** (-10) < cute_round(value, round_mode=RoundMode.ALWAYS_DOWN, step=step) < result + 10 ** (-10), \
            f"Error with value {value}, step {step}"

    @pytest.mark.parametrize("value, result", [(0, True), (4, True), (-1, True), (0.33 + 0.33 + 0.34, True),
                                               (21421, True), (23.214214, False), (0.00000000000001, False),
                                               (0.5 + 0.499999, False)])
    def test_is_integer(self, value, result):
        assert is_integer(value) is result, f"Error with value {value}"

    @pytest.mark.parametrize("number, result", [(-10, 3.5), (0, 3.5), (1, 3.5), (2, 3.5), (3, 3.5), (3.49, 3.5),
                                                (3.500001, 3.500001), (4, 4), (5, 5), (6, 6), (7, 7), (7.7999, 7.7999),
                                                (7.8001, 7.8), (8, 7.8), (9, 7.8), (100, 7.8)])
    def test_restrict_number_to_range(self, number, result):
        assert restrict_number_to_range(number, low_cutoff=3.5, high_cutoff=7.8) == result, f"Error in number {number}"

    @pytest.mark.parametrize("val_type", ["tuple", "list"])
    @pytest.mark.parametrize("values, result", [([1], 1), ([1, 2, 3], 6), ([2, 3, 1], 6), ([1, 2], 2),
                                                ([-1, -2, -3, -4], 24), ([1, 0, 141515, 0.215215, 214214.51255215], 0),
                                                ([1000, 1000, 0.001, 10000.5, -0.001, -2, -0.5], -10000.5),
                                                ([0, 0, 0, 0, 0, 0, 1], 0), ([], 1)])
    def test_product(self, values, result, val_type):
        if val_type == "list":
            values = list(values)
        elif val_type == "tuple":
            values = tuple(values)
        assert product(values) == result, f"Error with values {values}"

    infinity = float('inf')

    @pytest.mark.parametrize("numerator, denominator", [
                (infinity, 3), (infinity, 300.5), (infinity, -3), (infinity, -300.5),
                (-infinity, 3), (-infinity, 300.5), (-infinity, -3), (-infinity, -300.5),
                (3, infinity), (3, -infinity), (-3, infinity), (-3, -infinity),
                (300.5, infinity), (300.5, -infinity),
                (-300.5, infinity), (-300.5, -infinity),
                (0, infinity), (0, -infinity)
    ])
    def test_cute_div_inf(self, numerator, denominator):
        div, mod = cute_divmod(numerator, denominator)
        if abs(numerator) != float('inf'):
            assert div == cute_floor_div(numerator, denominator) == 0, f"Error with div for {numerator} / {denominator}"
            if (numerator != 0):
                assert numerator, f"Error with mod {mod} for {numerator} / {denominator}"
            else:
                assert math.isnan(mod), f"Error with mod {mod} for {numerator} / {denominator}"
        else:
            assert div == cute_floor_div(numerator, denominator) == float('Inf') * get_sign(denominator) * get_sign(numerator), \
                f"Error with div for {numerator} / {denominator}"
            assert math.isnan(mod), f"Error with mod {mod} for {numerator} / {denominator}"


