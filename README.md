bibextract
======

[![Build Status](https://img.shields.io/badge/release-1.0.0-orange)](https://github.com/arcunique/bibextract)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-371/)

__bibextract__ is a python module for extraction of information from a bibliography (.bib) file extremely useful for writing 
research articles and theses in LaTeX. This also allows users to go to the corresponding
[NASA ADS](https://ui.adsabs.harvard.edu/) site and the publisher's website for a particular article or journal.
This code can also be used to detect duplicate entries for an article.

Author
------
* Aritra Chakrabarty (IIA, Bangalore)

Requirements
------------
* python>3.6

Instructions on installation and use
------------------------------------
Presently, the code is only available on [Github](https://github.com/arcunique/bibextract). Download the code to use.

To use the code type:

from bibextract import bibtex\
bib = bibtex(filename)\

This __bib__ instance can be used to extract information as well as perform various taks, such as,

To get a dict object of article identifiers and dict object of information.\
print(bib.entries)

To open the publishers' websites of the articles using their identifiers (ids) and their DOIs.\
bib.open_doi(*ids)  

An example program (__example.py__) is shown for better understanding of the functionalities of the __bibextract__ 
module. 






