"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 206.835 - 1.015 x (words/sentences) - 84.6 x (syllables/words)

@category   Utility
@version    $Id: 0.1.1, 2015-06-03 16:48:47 ACST $;
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

        try:
            words_ps = 1.015 * (stats["words"] / float(stats["sentences"]))
            syl_pw = 84.6 * (stats["syllables"]['total'] / float(stats["words"]))
            results = 206.835 - words_ps - syl_pw
        except:
            results = 0

        return float("{0:.4f}".format(results))