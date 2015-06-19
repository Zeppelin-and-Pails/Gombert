"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 0.39 x (words/sentences) + 11.8 x (syllables/words) - 15.59

@category   Utility
@version    $Id: 0.1.1, 2015-06-03 16:48:47 ACST $;
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

        try:
            words_ps = 0.39 * (stats["words"] / float(stats["sentences"]))
            syl_pw = 11.8 * (stats["syllables"]['total'] / float(stats["words"]))
            results =  words_ps + syl_pw - 15.59
        except:
            results = 0

        return float("{0:.4f}".format(results))