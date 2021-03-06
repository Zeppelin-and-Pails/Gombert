"""
syllables

Stats package, given a body of text returns an approximate count of syllables (>90% accurate)

@category   Utility
@version    $ID: 1.1.1, 2015-05-30 17:00:00 CST $;
@author     KMR
@licence    http://www.wtfpl.net
"""
import re
import math

class textifier:
    def __init__(self):
        pass

    def basic_stats(self, text):
        stats = {}

        stats["characters"] = len(text)
        stats["characters (no spaces)"] = len(re.compile(r'[\s]+').sub('', text))
        stats["characters (alphanumeric only)"] = len(re.compile(r'[\W]+').sub('', text))
        stats["words"] = self.words(text)
        stats["sentences"] = self.sentences(text)
        stats["syllables"] = self.syllables(text)

        return stats

    def sentences(self, text):
        # Work out how many sentences there are
        words = re.sub(r'\s(?:dr.|mr.|bro.|mrs.|ms.|jr.|sr.|i.e.|e.g.|vs.)', "two" , text.lower())
        words = words.strip()
        return len(re.compile(r'\w[\.\?!]+[\'"\)\]]*').findall(words))

    def words(self, text):
        # Find out how many words there are
        words = re.compile(r'[\W]+').sub(' ', text.lower())
        words = words.strip()
        return len(re.compile("[\s]+").split(words))

    def unique_words(self, text):
        words = re.compile(r'[\W]+').sub(' ', text.lower())
        words = re.compile("[\s\W]+").split(words)
        seen = set()
        seen_add = seen.add
        uWords = [ x for x in words if not (x in seen or seen_add(x))]

        return uWords

    def syllables(self, text):
        syl_counts = {}
        syl_total = 0

        # Get the easy stuff out of the way first
        if len(text) == 1:
            syl_total = 1
        elif len(text) > 1:
            # If we've been given something substantial lets churn through it.
            vowels = 'aeiouy'
            words = re.compile("[\W]+").sub(' ', text.lower().strip())
            words = words.strip()
            words = re.compile("[\s]+").split(words)


            try:
                count = {"a":0, "b":0, "c":0}
                for word in words:
                    # First lets try one way
                    a = 0
                    if word[0] in vowels:
                        a += 1
                    for index in range(1,len(word)):
                        if word[index] in vowels and word[index-1] not in vowels:
                            a += 1
                    if (word.endswith('e') and  not word.endswith('le')):
                        a -= 1
                    if len(word) == 1:
                        a = 1
                    count['a'] += a

                    # Now lets try another
                    SubSyl = ["cial", "tia", "cius", "cious", "giu", "ion", "iou", "sia$", ".ely$"]
                    AddSyl = ["ia", "riet", "dien", "iu", "io", "ii", "[aeiou]{3}", "^mc", "ism$",
                              "[^aeiouy]{2}l$", "[^l]lien", "^coa[dglx].", "[^gq]ua[^auieo]", "dnt$"]

                    #if (word.endsWith("e")):
                    #    word = word.substring(0, word.length() - 1);

                    phonems = re.compile(r"[^aeiouy]+").split(word)

                    b = 0
                    for not_syl in SubSyl:
                        if not_syl in word:
                            b -= 1
                    for syl in AddSyl:
                        if syl in word:
                            b += 1
                    for phon in phonems:
                        if len(phon) > 0:
                            b += 1
                    if len(word) == 1:
                        b = 1
                    count['b'] += b

                    # And one last style
                    c = 0
                    on_vowel = False
                    in_diphthong = False
                    min = 0
                    max = 0
                    lastchar = None
                    vowels = 'aeiou'
                    for char in word:
                        is_vowel = char in vowels
                        if on_vowel == None:
                            on_vowel = is_vowel

                        # y is a special case
                        if char == 'y':
                            is_vowel = not on_vowel

                        if is_vowel:
                            if not on_vowel:
                                c += 1
                            elif on_vowel and not in_diphthong and char != lastchar:
                                in_diphthong = True
                                max += 1

                        on_vowel = is_vowel
                        lastchar = char

                    # Some special cases:
                    if word[-1] == 'e':
                        min -= 1
                    if word[-1] == 'y' and not on_vowel:
                        max += 1

                    c = math.ceil(((c + min) + (c + max)) / 2)
                    count['c'] += c

                    combined = math.ceil((a + b + c) / 3)

                    #combined = 1 if combined < 1
                    if combined in syl_counts:
                        syl_counts[combined] += 1
                    else :
                        syl_counts[combined] = 1
                # Mash them together and hope for the best
                syl_total = math.ceil((count['a'] + count['b'] + count['c']) / 3)
            except IndexError as err:
                pass

        return {"total" : syl_total, "counts" : syl_counts}
