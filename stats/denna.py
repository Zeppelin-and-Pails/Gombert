"""
Denna

A stats generation package, given a body of text will return a readability score

An attempt at creating a readability index for song lyrics


@category   Utility
@version    $Id: 0.1.1, 2015-06-03 16:48:47 ACST $;
@author     Jason
@licence    GNU GPL v3
"""
import textifier
import re
import lzw

class denna:

    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def determinRepetition(self, text):
        compressed = lzw.compress(text)
        sbytes     = str.encode(text.encode('utf8'))
        ratio      = float(len("".join(sbytes))) / float(len("".join(compressed)))

        return ratio

    def findPolysyllables(self, syllables):
        polysyllables = 0
        for count in syllables['counts']:
            if count > 2:
                polysyllables += syllables['counts'][count]

        return polysyllables

    def cleanText(self, text):
        non_alpha = re.compile(r"[^a-z\ \n]", re.IGNORECASE)
        return non_alpha.sub("", text).lower()

    def determinSongLength(self, text):
        return len(self.cleanText( text ))

    def process(self, text):
        stats               = self.tex.basic_stats(text)
        syl                 = self.tex.syllables(text)

        try:
            syllables       = float(syl['total'])
            repetition      = float(self.determinRepetition(text))
            polysyllables   = float(self.findPolysyllables(syl))
            uniqueWords     = filter(lambda x: len(x) > 3, self.tex.unique_words(text))
            songLength      = float(self.determinSongLength(text))

            d = ((( float( len(uniqueWords) ) / float( stats["words"] ) ) / ( syllables / (1 + polysyllables) )) / (repetition)) * 100
        except ValueError:
            d = 0
        except:
            d = 0

        return float("{0:.4f}".format( d ) )
