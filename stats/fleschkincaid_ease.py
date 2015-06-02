"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 206.835 - 1.015 x (words/sentences) - 84.6 x (syllables/words)

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
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