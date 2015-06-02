"""
SMOG (Simple Measure of Gobbledygook)

A stats generation package, given a body of text will return a readability score

uses 1.0430 x sqrt( 30 x complexWords/sentences ) + 3.1291

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import math
import textifier

class smog:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        syl = self.tex.syllables(text)
        complex = 0
        for count in syl['counts']:
            if count > 2:
                complex += syl['counts'][count]

        sentences = self.tex.sentences(text)

        return float("{0:.4f}".format((1.0430 * math.sqrt(30 * (complex/sentences))) + 3.1291))