=======
doi4bib
=======

A tiny utility to copy a bibtex file and enrich it with doi references


Description
===========

This small utility takes an existing bibtex file and outputs a copy of that file,
with additional Digital Object Identifier (DOI) references.

The DOI references are obtained by contacting the CrossRef API.
The code to contact the API was shamelessly copied from the OpenAPC DOI Importer
https://github.com/OpenAPC/openapc-de/blob/master/python/import_dois.py
to whom I owe a lot of gratitude.

Note
====

This project has been set up using PyScaffold 3.2.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
