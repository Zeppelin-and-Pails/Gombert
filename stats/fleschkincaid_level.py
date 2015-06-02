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
        stats = self.tex.basic_stats(text)

        words_ps = 0.39 * (stats["words"] / float(stats["sentences"]))
        syl_pw = 11.8 * (stats["syllables"]['total'] / float(stats["words"]))

        return float("{0:.4f}".format( words_ps + syl_pw - 15.59))