import sys
import os
import pytest
import numpy as np

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_CODE_EX02 = os.path.abspath(os.path.join(CURRENT_DIR, '../../ex02'))
sys.path.insert(0, SRC_CODE_EX02)


from load_image import ft_load


def test_non_str_param_prints_error(capsys):
    result = ft_load(82)
    captured = capsys.readouterr()

    assert "Assertion error" in captured.out
    assert "The path must be a string" in captured.out


def test_invalid_format(capsys):
    result = ft_load("arrow.png")
    captured = capsys.readouterr()

    assert "Assertion error" in captured.out
    assert "Only .jpg or .jpeg file extensions are allowed" in captured.out


def test_no_file_found(capsys):
    filename = "nosuchfile.jpg"
    result = ft_load(filename)
    captured = capsys.readouterr()

    # assert "Assertion error" in captured.out
    assert "Error:  [Errno 2] No such file or directory: '" + filename + "'" in captured.out