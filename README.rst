=======
doi4bib
=======

A tiny utility to copy a bibtex file and enrich it with DOI references.

.. image:: https://travis-ci.com/sharkovsky/doi4bib.svg?branch=master
    :target: https://travis-ci.com/sharkovsky/doi4bib

Description
===========

This small utility takes an existing bibtex file and outputs a copy of that file,
with additional Digital Object Identifier (DOI) references.

Installation
============

To install all the dependencies, clone this repository and navigate to it.
Then run::

    python setup.py install

Note: it requires Python 3.


Usage
=====

::

    doi4bib [-h] [-o OUT_FILE] [--version] [-v] [-vv] bib_file

where ``bib_file`` is a bibtex file that you want to enrich with DOI references.
It will output a copy of that file, in which each entry has been endowed with
the DOI reference to that article.

The DOI reference is obtained by contacting the `Crossref REST API`_

Note
====

The DOI references are obtained by contacting the Crossref API.
The code to contact the API was shamelessly copied from the
`OpenAPC DOI Importer`_ by the `OpenAPC initiave`_ to whom I owe a lot of
gratitude.

I am using aclement's biblib_ to parse bibtex files, to whom I also owe
a lot of gratitude.

This project has been set up using PyScaffold 3.2.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.

.. _Crossref REST API: https://github.com/CrossRef/rest-api-doc.
.. _OpenAPC DOI Importer: https://github.com/OpenAPC/openapc-de/blob/master/python/import_dois.py
.. _OpenAPC initiave: https://treemaps.intact-project.org/
.. _biblib: https://github.com/aclements/biblib
