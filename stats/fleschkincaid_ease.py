"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 206.835 - 1.015 x (words/sentences) - 84.6 x (syllables/words)

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import textifier

class fleschkincaid_ease:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        syl = self.tex.syllables(text)['total']
        words = self.tex.words(text)
        sentences = self.tex.sentences(text)

        return float("{0:.4f}".format(206.835 - (1.015 * (words/sentences)) - (84.6 * (syl/words))))