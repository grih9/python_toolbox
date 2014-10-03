

from python_toolbox.math_tools import abs_stirling, calculate_length_of_recurrent_perm_space, calculate_length_of_recurrent_comb_space


def test_abs_stirling():
    assert tuple(abs_stirling(0, i) for i in range(-1, 2)) == (0, 1, 0, )
    assert tuple(abs_stirling(1, i) for i in range(-1, 3)) == (0, 0, 1, 0, )
    assert tuple(abs_stirling(2, i) for i in range(-1, 4)) == (0, 0, 1, 1, 0)
    assert tuple(abs_stirling(3, i) for i in range(-1, 5)) == (0, 0, 2, 3, 1,
                                                               0)
    assert tuple(abs_stirling(4, i) for i in range(-1, 6)) == (0, 0, 6, 11, 6,
                                                               1, 0)
    assert tuple(abs_stirling(5, i) for i in range(-1, 7)) == (0, 0, 24, 50,
                                                               35, 10, 1, 0)
    
    assert abs_stirling(200, 50) == 525010571470323062300307763288024029929662200077890908912803398279686186838073914722860457474159887042512346530620756231465891831828236378945598188429630326359716300315479010640625526167635598138598969330736141913019490812196987045505021083120744610946447254207252791218757775609887718753072629854788563118348792912143712216969484697600


def test_recurrent_perm_space_length():
    assert calculate_length_of_recurrent_perm_space(3, (3, 1, 1)) == 13
    assert calculate_length_of_recurrent_perm_space(2, (3, 2, 2, 1)) == 15
    assert calculate_length_of_recurrent_perm_space(3, (3, 2, 2, 1)) == 52
    

def test_recurrent_comb_space_length():
    assert calculate_length_of_recurrent_comb_space(3, (3, 1, 1)) == 4
    assert calculate_length_of_recurrent_comb_space(2, (3, 2, 2, 1)) == 9
    assert calculate_length_of_recurrent_comb_space(3, (3, 2, 2, 1)) == 14
    