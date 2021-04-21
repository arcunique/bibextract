from bibextract import bibtex
import sys


file = sys.argv[1]
bib = bibtex(file)
bib.open_ads('birkby13','birkby17')
