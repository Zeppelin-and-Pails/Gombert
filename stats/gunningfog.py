"""
Gunning Fog

A stats generation package, given a body of text will return a readability score

uses 0.4 x ( (words/sentences) + 100 x (complexWords/words) )

@category   Utility
@version    $Id: 0.1.1, 2015-06-03 16:48:47 ACST $;
@author     KMR
@licence    GNU GPL v3
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

        try:
            words = self.tex.words(text)
            sentences = self.tex.sentences(text)
            results = 0.4 * ((words/float(sentences)) + 100 * (complex/float(words)))
        except:
            results = 0

        return float("{0:.4f}".format(results))
