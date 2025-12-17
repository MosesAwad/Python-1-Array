import sys
import os
import pytest
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_CODE_EX01 = os.path.abspath(os.path.join(CURRENT_DIR, '../../ex01'))
sys.path.insert(0, SRC_CODE_EX01)

from array2D import slice_me


def test_valid_arguments():
    valid_2D = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    result = slice_me(valid_2D, 0, 2)
    assert np.array_equal(
        result,
        np.array([
            [1.80, 78.4],
            [2.15, 102.7]
        ])
    )

    result = slice_me(valid_2D, 1, 2)
    assert np.array_equal(
        result,
        np.array([
            [2.15, 102.7]
        ])
    )


def test_not_list_argument():
    not_list = (
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    )
    result = slice_me(not_list, 0, 2)
    assert result is None


def test_1D_list_argument():
    one_dimensional_list = [
        1.80, 78.4, 2.15, 102.7, 2.10, 98.5, 1.88, 75.2
    ]
    result = slice_me(one_dimensional_list, 0, 2)
    assert result is None


def test_not_2D_list_argument():
    invalid_2D = [
        [1.80, 78.4],
        [2.15, 102.7],
        {2.10, 98.5},
        [1.88, 75.2]
    ]
    result = slice_me(invalid_2D, 0, 2)
    assert result is None


def test_jagged_array():
    jagged_array = [
        [1.80],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    result = slice_me(jagged_array, 0, 2)
    assert result is None


def test_start_end_invalid_values():
    valid_2D = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    result = slice_me(valid_2D, 1, 'a')
    assert result is None

    result = slice_me(valid_2D, 'a', 2)
    assert result is None

    result = slice_me(valid_2D, 'c', 'a')
    assert result is None
