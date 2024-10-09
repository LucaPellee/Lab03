import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self._italian = d.Dictionary([],"italian")
        self._english = d.Dictionary([], "english")
        self._spanish = d.Dictionary([], "spanish")
        self._italian.loadDictionary('resources/Italian.txt')
        self._english.loadDictionary('resources/English.txt')
        self._spanish.loadDictionary('resources/Spanish.txt')

    def printDic(self, language):
        if language == "italian":
            self._italian.printAll()
        elif language == "english":
            self._english.printAll()
        elif language == "spanish":
            self._spanish.printAll()

    def searchWord(self, words, language):
        parole_err = []
        for w in words:
            parola = rw.RichWord(w)
            if language == "italian":
                if w in self._italian:
                    parola.corretta = True
                else:
                    parole_err.append(parola)
            if language == "english":
                if w in self._english:
                    parola.corretta = True
                else:
                    parole_err.append(parola)
            if language == "spanish":
                if w in self._spanish:
                    parola.corretta = True
                else:
                    parole_err.append(parola)
        return parole_err

    def searchWordLinear(self, words,language):
        parole_err = []
        for w in words:
            found = False
            parola = rw.RichWord(w)
            if language == "italian":
                for p in self._italian.dict:
                    if p == w:
                        parola.corretta = True
                        found = True
                if found == False:
                    parole_err.append(parola)
            if language == "english":
                for p in self._english.dict:
                    if p == w:
                        parola.corretta = True
                        found = True
                if found == False:
                    parole_err.append(parola)
            if language == "spanish":
                for p in self._spanish.dict:
                    if p == w:
                        parola.corretta = True
                        found = True
                if found == False:
                    parole_err.append(parola)
        return parole_err

    def searchWordDichotomic(self, words, language):
        parole_err = []
        for w in words:
            found = False
            parola = rw.RichWord(w)
            if language == "italian":
                currentDict = self._italian.dict
                found = self.dichotomic(currentDict, w)
                if found == True:
                    parola.corretta = True
                else:
                    parole_err.append(parola)

            if language == "english":
                currentDict = self._english.dict
                found = self.dichotomic(currentDict, w)
                if found == True:
                    parola.corretta = True
                else:
                    parole_err.append(parola)

            if language == "spanish":
                currentDict = self._spanish.dict
                found = self.dichotomic(currentDict, w)
                if found == True:
                    parola.corretta = True
                else:
                    parole_err.append(parola)
        return parole_err


    def dichotomic(self, currentDict, word):
        start = 0
        end = len(currentDict)
        while (start != end):
            mean = start + int((end - start) / 2)
            if word == currentDict[mean]:
                return True
            elif word > currentDict[mean]:
                start = mean + 1
            else:
                end = mean
        return False

