import pytest

from python_toolbox.math_tools import abs_stirling, stirling, get_sign


def test_stirlig_sign():
    for k in range(1, 1000):
        for n in range(k + 1, 1001):
            if (n + k) % 2 == 0:
                assert get_sign(stirling(n, k)) == 1, f"n={n}, k={k}"
            else:
                assert get_sign(stirling(n, k)) == -1, f"n={n}, k={k}"


@pytest.mark.parametrize("n, k_range, result", [(0, 2, (0, 1, 0)), (1, 3, (0, 0, 1, 0)), (2, 4, (0, 0, 1, 1, 0)),
                                                (3, 5, (0, 0, 2, 3, 1, 0)), (4, 6, (0, 0, 6, 11, 6, 1, 0)),
                                                (5, 7, (0, 0, 24, 50, 35, 10, 1, 0)),
                                                (250, 73, 421764292651512234017061328819044113599063358009853129334853754650715777870518099267785075443553532888033922011632541187496172452114596129734300255023103690312000089790301997686454309504092376879152135117187723117924042443958020954487333012930225623594609389788498623629546672495543793620137500495662444934248868919581663992219255633886252520154242314792534078298516736231125523589942812923693653119222827005959680819200000)])
def test_abs_stirling(n, k_range, result):
    if not isinstance(result, tuple):
        assert abs_stirling(n=n, k=k_range) == result
    else:
        assert tuple(abs_stirling(n=n, k=i) for i in range(-1, k_range)) == result
    # The number was verified with Wolfram Mathematica.

