"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 0.39 x (words/sentences) + 11.8 x (syllables/words) - 15.59

@category   Utility
@version    $Id: 0.1.0, 2015-06-03 13:32:04 ACST $;
@author     KMR
@licence    GNU GPL v3
"""
import textifier

class fleschkincaid_level:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        stats = self.tex.basic_stats(text)

        words_ps = 0.39 * (stats["words"] / float(stats["sentences"]))
        syl_pw = 11.8 * (stats["syllables"]['total'] / float(stats["words"]))

        return float("{0:.4f}".format( words_ps + syl_pw - 15.59))