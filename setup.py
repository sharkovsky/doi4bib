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

if __name__ == "__main__":
    setup(  # use_pyscaffold=True
            name='doi4bib',
            packages=['doi4bib'],
            use_scm_version=True,
            setup_requires=['unidecode', 'pyyaml', 'setuptools_scm'],
            install_requires=[
                'python-Levenshtein',
                'biblib@git+https://github.com/\
aclements/biblib.git#egg=biblib-0.1.0'
                ],
            dependency_links=[
                'git+https://github.com/aclements/biblib.git#egg=biblib-0.1.0'
                ],
            tests_require=[
                'pytest',
                'pytest-cov',
                'flake8'
                ],
            python_requires='>=3.5'
            )
