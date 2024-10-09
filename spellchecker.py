

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self._multiDict = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()

        return self._multiDict.searchWord(words, language)

    def handleSentenceLinear(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()
        return self._multiDict.searchWordLinear(words, language)

    def handleSentenceDichotomic(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()
        return self._multiDict.searchWordDichotomic(words, language)


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text