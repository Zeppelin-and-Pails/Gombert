"""
Denna

A stats generation package, given a body of text will return a readability score

An attempt at creating a readability index for song lyrics

uses 0.39 x (words/unique words > 3 characters) + 11.8 x (syllables/words)

@category   Utility
@version    $Id: 0.1.0, 2015-06-03 13:32:04 ACST $;
@author      Jason
@licence    GNU GPL v3
"""
import textifier
class denna:

    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        stats = self.tex.basic_stats(text)

        uniqueWords = filter(lambda x: len(x) > 3, self.tex.unique_words(text))
        words_ps = 0.39 * (stats["words"] / float(len(uniqueWords)))
        syl_pw = 11.8 * (stats["syllables"]['total'] / float(stats["words"]))

        return float("{0:.4f}".format(words_ps + syl_pw))
