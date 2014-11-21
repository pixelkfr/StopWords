#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Build a stopwords list in a language, given in parameters
How to use it : python StopWordsList.py language
To put it in a file, use the commande line followed by " > fileOut.txt "
"""
import sys
from nltk.corpus import stopwords

language = sys.argv[1]

for word in stopwords.words(language):
    print word.encode("utf-8")

