import spellchecker
import time

sc = spellchecker.SpellChecker()

while(True):
    sc.printMenu()

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        t1 = time.time()
        lista = sc.handleSentence(txtIn,"italian")
        t2 = time.time()
        print("Ricerca con contains: "+ str(t2-t1))
        if len(lista) >0:
            for parola in lista:
                print(parola)
        else:
            print("Parole tutte corrette")

        t3 = time.time()
        lista1 = sc.handleSentenceLinear(txtIn,"italian")
        t4 = time.time()
        print("Ricerca lineare: "+ str(t4-t3))
        if len(lista1) >0:
            for parola in lista1:
                print(parola)
        else:
            print("Parole tutte corrette")

        t5 = time.time()
        lista2 = sc.handleSentenceDichotomic(txtIn,"italian")
        t6 = time.time()
        print("Ricerca dicotomica: "+ str(t6-t5))
        if len(lista2) >0:
            for parola in lista2:
                print(parola)
        else:
            print("Parole tutte corrette")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        t1 = time.time()
        lista = sc.handleSentence(txtIn, "english")
        t2 = time.time()
        print("Ricerca con contains: " + str(t2 - t1))
        if len(lista) > 0:
            for parola in lista:
                print(parola)
        else:
            print("Parole tutte corrette")

        t3 = time.time()
        lista1 = sc.handleSentenceLinear(txtIn, "english")
        t4 = time.time()
        print("Ricerca lineare: " + str(t4 - t3))
        if len(lista1) > 0:
            for parola in lista1:
                print(parola)
        else:
            print("Parole tutte corrette")

        t5 = time.time()
        lista2 = sc.handleSentenceDichotomic(txtIn, "english")
        t6 = time.time()
        print("Ricerca dicotomica: " + str(t6 - t5))
        if len(lista2) > 0:
            for parola in lista2:
                print(parola)
        else:
            print("Parole tutte corrette")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        t1 = time.time()
        lista = sc.handleSentence(txtIn, "spanish")
        t2 = time.time()
        print("Ricerca con contains: " + str(t2 - t1))
        if len(lista) > 0:
            for parola in lista:
                print(parola)
        else:
            print("Parole tutte corrette")

        t3 = time.time()
        lista1 = sc.handleSentenceLinear(txtIn, "spanish")
        t4 = time.time()
        print("Ricerca lineare: " + str(t4 - t3))
        if len(lista1) > 0:
            for parola in lista1:
                print(parola)
        else:
            print("Parole tutte corrette")

        t5 = time.time()
        lista2 = sc.handleSentenceDichotomic(txtIn, "spanish")
        t6 = time.time()
        print("Ricerca dicotomica: " + str(t6 - t5))
        if len(lista2) > 0:
            for parola in lista2:
                print(parola)
        else:
            print("Parole tutte corrette")
        continue

    if int(txtIn) == 4:
        break


