"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 0.39 x (words/sentences) + 11.8 x (syllables/words) - 15.59

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import textifier

class fleschkincaid_level:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        syl = self.tex.syllables(text)['total']
        words = self.tex.words(text)
        sentences = self.tex.sentences(text)

        return float("{0:.4f}".format((0.39 * (words/sentences)) + (11.8 * (syl/words)) - 15.59))