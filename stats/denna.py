"""
Denna

A stats generation package, given a body of text will return a readability score

An attempt at creating a readability index for song lyrics

uses 0.39 x (words/unique words > 3 characters) + 11.8 x (syllables/words)

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     Jason
@licence    http://www.wtfpl.net
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
