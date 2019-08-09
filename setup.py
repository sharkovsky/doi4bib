# -*- coding: utf-8 -*-
"""
    Setup file for doi4bib.
    Use setup.cfg to configure your project.

    This file was generated with PyScaffold 3.2.1.
    PyScaffold helps you to put up the scaffold of your new Python project.
    Learn more under: https://pyscaffold.org/
"""
import sys

from pkg_resources import VersionConflict, require
from setuptools import setup

try:
    require('setuptools>=38.3')
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)

URL_OF_BIBLIB_EGG = 'https://github.com/aclements/biblib/tarball/master/'

if __name__ == "__main__":
    setup(use_pyscaffold=True,
          install_requires=[
              'biblib==0.1.0',
              'python-Levenshtein',
              ],
          dependency_links=[
              URL_OF_BIBLIB_EGG + '#egg=biblib-0.1.0'
              ])
