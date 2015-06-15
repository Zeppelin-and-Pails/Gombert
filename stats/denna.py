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
import re

class denna:

    tex = None

    def __init__(self):
        self.tex = textifier.textifier()

    def getPhrases(self, words, limit):
        phrase = []
        for word in words:
            phrase.append(word)
            if len(phrase) > limit:
                phrase.remove(phrase[0])
            if len(phrase) == limit:
                yield tuple(phrase)

    def getWords(self, text):
        pattern = re.compile(r"[^\s]+")
        non_alpha = re.compile(r"[^a-z]", re.IGNORECASE)
        for match in pattern.finditer(text):
            yield non_alpha.sub("", match.group()).lower()

    def getSentences(self, text):
        text = re.sub( '\n\n', '\n', text ).strip()
        return text.splitlines()

    def uniqueList(self, seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if not (x in seen or seen_add(x))]

    def cleanText(self, text):
        non_alpha = re.compile(r"[^a-z\ \n]", re.IGNORECASE)
        return non_alpha.sub("", text).lower()

    def findLongestPhrases(self, uniqPhrases):
        longestPhrases = []

        for found in uniqPhrases:
            f = filter(lambda x: found in x, uniqPhrases)
            if len( f ) > 1:
                maxf = max(f, key=len)
                uniqPhrases = filter(lambda a: a != maxf, uniqPhrases)
                longestPhrases.append(maxf)

        return longestPhrases

    def determinRepetition(self, text):
        scannedSentances = []
        foundPhrases = []
        longestPhrases = []
        text = self.cleanText( text )
        sentances = self.getSentences(text)
        totalRepeats = 0

        longestSentanceLength = len(max( sentances, key=len))

        for sentance in sentances:
            if sentance not in scannedSentances:
                tcount = text.count(sentance)
                if tcount > 1:
                    scannedSentances.append(sentance)
                    totalRepeats += tcount
                    #print "Repeated sentance: '{}' repeated {} times".format(sentance, tcount)
                    sentances = filter(lambda a: a != sentance, sentances)

        for sentanceLength in range(3, longestSentanceLength):
            for sentance in sentances:
                results = list(self.getPhrases(self.getWords(sentance), sentanceLength ))
                if results:
                    for phrase in results:
                        foundPhrases.append( ' '.join( phrase ) )

        uniqPhrases = self.uniqueList(foundPhrases)

        longestPhrases = self.findLongestPhrases(uniqPhrases)

        for phrase in longestPhrases:
            tcount = text.count(phrase)
            if tcount > 1:
                #print "Repeated phrase: '{}' repeated {} times".format(phrase, tcount)
                totalRepeats += tcount

        return totalRepeats

    def findPolysyllables(self, syllables):
        polysyllables = 0
        for count in syllables['counts']:
            if count > 2:
                polysyllables += syllables['counts'][count]

        return polysyllables

    def determinSongLength(self, text):
        return len(self.cleanText( text ))

    def process(self, text):
        stats           = self.tex.basic_stats(text)
        syl             = self.tex.syllables(text)
        uniqueWords     = filter(lambda x: len(x) > 3, self.tex.unique_words(text))
        polysyllables   = float(self.findPolysyllables(syl))
        repetition      = float(self.determinRepetition(text))
        songLength      = float(self.determinSongLength(text))
        syllables       = float(syl['total'])

        return float("{0:.4f}".format( ((( float( len(uniqueWords) ) / float( stats["words"] ) ) / ( syllables / (1 + polysyllables) )) * (12.0 + ( repetition / songLength) )) * 100 ) )
