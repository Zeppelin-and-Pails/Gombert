"""
Gunning Fog

A stats generation package, given a body of text will return a readability score

uses 0.4 x ( (words/sentences) + 100 x (complexWords/words) )

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import textifier

class gunningfog:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        syl = self.tex.syllables(text)
        complex = 0
        for count in syl['counts']:
            if count > 2:
                complex += syl['counts'][count]

        words = self.tex.words(text)
        sentences = self.tex.sentences(text)

        return float("{0:.4f}".format(0.4 * ((words/sentences) + 100 * (complex/words))))
