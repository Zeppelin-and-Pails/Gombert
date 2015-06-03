"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 206.835 - 1.015 x (words/sentences) - 84.6 x (syllables/words)

@category   Utility
@version    $Id: 0.1.0, 2015-06-03 13:32:04 ACST $;
@author     KMR
@licence    GNU GPL v3
"""
import textifier

class fleschkincaid_ease:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        stats = self.tex.basic_stats(text)
        words_ps = 1.015 * (stats["words"] / float(stats["sentences"]))
        syl_pw = 84.6 * (stats["syllables"]['total'] / float(stats["words"]))

        return float("{0:.4f}".format(206.835 - words_ps - syl_pw))