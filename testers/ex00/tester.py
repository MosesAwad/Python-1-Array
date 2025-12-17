import sys
import os
import pytest

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_CODE_EX00 = os.path.abspath(os.path.join(CURRENT_DIR, '../../ex00'))
sys.path.insert(0, SRC_CODE_EX00)

from give_bmi import give_bmi, apply_limit


def test_give_bmi_and_apply_limit():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)

    assert bmi == pytest.approx(
        [22.507863455018317, 29.0359168241966],
        rel=1e-9
    )

    result = apply_limit(bmi, 26)
    assert result == [False, True]


def test_give_bmi_height_and_weight_lists_not_equal_in_length():
    height_list = [1.72, 1.83, 1.92, 1.62, 1.58]
    weight_list = [115, 78, 91, 69]
    result = give_bmi(height_list, weight_list)
    assert result is None


def test_give_bmi_invalid_values_for_height_and_weight_lists():
    height_list = [1.72, 1.83, -1.92, 1.62, 1.58]
    weight_list = [115, 78, 91, 69, 72]
    result = give_bmi(height_list, weight_list)
    assert result is None

    height_list = [1.72, 1.83, 1.92, 1.62, 1.58]
    weight_list = [115, 78, -91, 69, 72]
    result = give_bmi(height_list, weight_list)
    assert result is None


    height_list = [1.72, -1.83, 1.92, 1.62, 1.58]
    weight_list = [115, 78, 91, -69, 72]
    result = give_bmi(height_list, weight_list)
    assert result is None


def test_give_bmi_not_list_arguments():
    height = {1.72, 1.83}
    weight = [82, 87]    
    result = give_bmi(height, weight)
    assert result is None

    height = [1.72, 1.83]
    weight = {82, 87}
    result = give_bmi(height, weight)
    assert result is None

    height = {1.72, 1.83}
    weight = {82, 87}
    result = give_bmi(height, weight)
    assert result is None


def test_apply_limit_invalid_list_contents():
    bad_list = [28.32, 22.10, 24.87, 'a']
    result = apply_limit(bad_list, 26)
    assert result is None


def test_apply_limit_not_a_list():
    not_a_list = {23.40, 25.20, 21.92}
    result = apply_limit(not_a_list, 26)
    assert result is None


def test_apply_limit_non_int_value_for_limit_param():
    good_list = [22.507863455018317, 29.0359168241966]
    result = apply_limit(good_list, "not an int hahaha")
    assert result is None
