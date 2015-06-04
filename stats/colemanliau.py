"""
Coleman Liau

A stats generation package, given a body of text will return a readability score

uses ( 0.0588 x (( characters / words ) x 100 ) - ( 0.296 x (( sentences / words ) * 100 ) - 15.8

@category   Utility
@version    $Id: 0.1.1, 2015-06-03 16:48:47 ACST $;
@author     KMR
@licence    GNU GPL v3
"""
import textifier

class colemanliau:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        stats = self.tex.basic_stats(text)
        char_pw = ((5.89 * stats["characters (alphanumeric only)"]) / float(stats["words"]))
        sentences_pw = ((29.6 * stats["sentences"]) / float(stats["words"]))

        return float("{0:.4f}".format(char_pw - sentences_pw - 15.8))