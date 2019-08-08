# -*- coding: utf-8 -*-

import pytest
from doi4bib.skeleton import fib

__author__ = "sharkovsky"
__copyright__ = "sharkovsky"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
