"""
Automated Readability Index (ARI)

A stats generation package, given a body of text will return a readability score

uses 4.71 x (characters/words) + 0.5 x (words/sentences) - 21.43

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import textifier

class ari:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        words = self.tex.words(text)
        sentences = self.tex.sentences(text)
        chars = len(text.lower().strip("\s"))

        return float("{0:.4f}".format((4.71 * (chars/words)) + (0.5 * (words/sentences)) - 21.43))