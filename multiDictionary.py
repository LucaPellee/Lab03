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


