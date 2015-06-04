"""
Denna

A stats generation package, given a body of text will return a readability score

An attempt at creating a readability index for song lyrics


@category   Utility
@version    $Id: 0.1.1, 2015-06-03 16:48:47 ACST $;
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
        syl = self.tex.syllables(text)
        uniqueWords = filter(lambda x: len(x) > 3, self.tex.unique_words(text))

        polysyllables = 0
        for count in syl['counts']:
            if count > 2:
                polysyllables += syl['counts'][count]


        uw = (len(uniqueWords) / stats["words"]) + polysyllables
     
        return float("{0:.4f}".format( uw ))
