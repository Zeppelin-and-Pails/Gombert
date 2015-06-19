"""
Automated Readability Index (ARI)

A stats generation package, given a body of text will return a readability score

uses 4.71 x (characters/words) + 0.5 x (words/sentences) - 21.43

@category   Utility
@version    $Id: 0.1.1, 2015-06-03 16:48:47 ACST $;
@author     KMR
@licence    GNU GPL v3
"""
import re
import textifier

class ari:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        stats = self.tex.basic_stats(text)
        try:
            char_pw = 4.71 * (stats["characters (no spaces)"] / float(stats["words"]))
            words_ps = 0.5 * (stats["words"] / float(stats["sentences"]))
            results = char_pw + words_ps - 21.43
        except:
            results = 0

        return float("{0:.4f}".format(results))