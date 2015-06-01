"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 206.835 - 1.015 x (words/sentences) - 84.6 x (syllables/words)

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import re
import math
import textifier

class fleschkincaid_ease:
    tex = textifier.textifier()

    def __init__(self):
        pass

    def process(self, text):
        syl = self.tex.syllables(text);

        words = text.lower().strip(".:;?!")
        words = re.compile("[\s\W]+").split(words)

        sentences = self.tex.sentences(text)


        return "hello"