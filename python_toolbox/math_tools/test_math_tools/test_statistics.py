import pytest

from python_toolbox.math_tools import get_median, get_mean


@pytest.mark.parametrize("val_type", ["tuple", "list"])
class TestStatistics:

    @pytest.mark.parametrize("values, median", [([1], 1), ([1, 2, 3], 2), ([2, 3, 1], 2), ([1, 2], 1.5),
                                                ([1, 2, 3, 4], 2.5), ([1000, 1000, -2, 10000.5, -4, -14, -50.5], -2),
                                                ([10000.5, -2, -4, -14, -50.5], -4), ([0, 0, 0, 0, 0, 0, 1], 0),
                                                ([float('inf'), 2, 54, -float('inf')], 28), ([], None)])
    def test_median(self, values, median, val_type):
        if median is None:
            with pytest.raises(AssertionError):
                get_median(values)
            return
        if val_type == "list":
            values = list(values)
        elif val_type == "tuple":
            values = tuple(values)
        assert get_median(values) == median

    @pytest.mark.parametrize("values, mean", [([1], 1), ([1, 2, 3], 2), ([2, 3, 1], 2), ([1, 2], 1.5),
                                              ([1, 2, 3, 4], 2.5), ([-1, -2, -3, -4, -5], -3), ([-10000, 10000], 0),
                                              ([100.5, -2, -4, -14, -50.5], 6), ([0, 0, 0, 0, 1], 0.2),
                                              ([0, 0, 0, 0, -1], -0.2), ([], 0)])
    def test_mean(self, values, mean, val_type):
        if val_type == "list":
            values = list(values)
        elif val_type == "tuple":
            values = tuple(values)
        assert get_mean(values) == mean, f"Error with values {values}"
