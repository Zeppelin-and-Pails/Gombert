"""
Coleman Liau

A stats generation package, given a body of text will return a readability score

uses ( 0.0588 x (( characters / words ) x 100 ) - ( 0.296 x (( sentences / words ) * 100 ) - 15.8

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import textifier

class colemanliau:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        words = self.tex.words(text)
        sentences = self.tex.sentences(text)
        chars = len(text.lower().strip("\s"))

        return float("{0:.4f}".format(((5.89*chars)/float(words)) - ((29.6*sentences)/float(words)) - 15.8))