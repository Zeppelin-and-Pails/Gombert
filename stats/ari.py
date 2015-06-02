"""
Automated Readability Index (ARI)

A stats generation package, given a body of text will return a readability score

uses 4.71 x (characters/words) + 0.5 x (words/sentences) - 21.43

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import re
import textifier

class ari:
    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        stats = self.tex.basic_stats(text)
        char_pw = 4.71 * (stats["characters (no spaces)"] / float(stats["words"]))
        words_ps = 0.5 * (stats["words"] / float(stats["sentences"]))


        return float("{0:.4f}".format(char_pw + words_ps - 21.43))