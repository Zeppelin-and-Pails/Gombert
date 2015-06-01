"""
Flesch-Kincaid

A stats generation package, given a body of text will return a readability score

uses 0.39 x (words/sentences) + 11.8 x (syllables/words) - 15.59

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import math
import textifier

class fleschkincaid:
    def process(self, text):
        syl = textifier.syllables(text);

        words = text.lower().strip(".:;?!")
        words = re.compile("[\s\W]+").split(words)

        sentences = textifier.sentences(text)



        return "hello"