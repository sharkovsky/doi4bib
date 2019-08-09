# -*- coding: utf-8 -*-

from doi4bib import add_dois_to_bib

__author__ = "sharkovsky"
__copyright__ = "sharkovsky"
__license__ = "mit"


def test_handle_empty_db():
    assert len(add_dois_to_bib(dict()).keys()) == 0
