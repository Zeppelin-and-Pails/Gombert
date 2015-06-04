"""
LIX

A stats generation package, given a body of text will return a readability score

uses (words / periods) + (longWords x 100 / words)

- full stops or colons count as periods
- words longer than 6 letters are long words

@category   Utility
@version    $Id: 0.1.0, 2015-06-03 13:32:04 ACST $;
@author      Jason
@licence    GNU GPL v3
"""
import re
import textifier

class lix:
    tex = None
    def __init__(self):
        self.tex = textifier.textifier()

    def process(self, text):
        words = float(self.tex.words(text))

        periods = len(re.compile(r'[\.\:]').findall(text))

        text = re.compile(r'[\W]+').sub(' ', text.lower())
        text = re.compile("[\s]+").split(text)

        longwords = filter(lambda x: len(x) > 6, text)

        words_pp = (words / periods) if periods > 0 else 0
        long_pw = (100 * len(longwords) / words)
        print words_pp
        print long_pw

        return int("{0:.0f}".format(words_pp + long_pw))
