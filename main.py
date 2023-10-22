numere_complexe = []


def alegere_optiune():
    try:
        p = int(input("Alege o optiune: "))
        return p
    except ValueError:
        print("Datele nu sunt introduse corect")


def citire_nr_complex():
    try:
        real = int(input("Dati partea reala: "))
        imag = int(input("Dati partea imaginara: "))
        return complex(real, imag)
    except ValueError:
        print("Datele nu au fost introduse corect!")


def citire_index():
    try:
        index = int(input("Dati un index: "))
        return index
    except ValueError:
        print("Datele nu au fost introduse corect!")


def test_add_la_final():
    lista = [(1+2j), (5+4j)]
    numar = (13+20j)
    assert add_la_final(numar, lista) == [(1+2j), (5+4j), (13+20j)]


def add_la_final(numar, lista):
    lista.append(numar)
    return lista


def test_add_cu_index():
    lista = [(3+4j), (7+8j), (5+9j)]
    numar = (14+17j)
    index = 1
    assert add_cu_index(numar, index, lista) == [(3+4j), (7+8j), (14+17j), (5+9j)]


def add_cu_index(numar, index, lista):
    try:
        lista.insert(index+1, numar)
        return lista
    except IndexError:
        print("Nu s-a gasit indexul dat")
        return -1


def test_stergere_numar():
    lista = [(3+4j), (5+7j), (9+8j), (14+15j)]
    index = 2
    assert stergere_numar(index, lista) == [(3+4j), (5+7j), (14+15j)]


def stergere_numar(index, lista):
    try:
        del lista[index]
        return lista
    except IndexError:
        print("Nu există un număr pe această poziție!")
        return -1


def test_stergere_interval():
    lista = [(1+2j), (3+4j), (5+6j), (7+8j), (4+10j)]
    start = 1
    stop = 4
    assert stergere_interval(start, stop, lista) == [(1+2j), (4+10j)]


def stergere_interval(start, stop, lista):
    try:
        del lista[start:stop]
        return lista
    except IndexError:
        print("Intervalul dat nu există în listă")
        return -1


def test_inlocuire_numar():
    lista = [(1+2j), (5+7j), (1+2j), (24+13j), (1+2j)]
    inlocuitor = (3+4j)
    inlocuit = (1+2j)
    assert inlocuire_numar(inlocuit, inlocuitor, lista) == [0, 2, 4]


def inlocuire_numar(inlocuit, inlocuitor, lista):
    lista_aux = []
    for i in range(0, len(lista)):
        if lista[i] == inlocuit:
            lista[i] = inlocuitor
            lista_aux.append(i)
    return lista_aux


def test_parte_imag():
    lista = [(1+2j), (3+4j), (7+8j)]
    assert parte_imag(0, 2, lista) == [2.0, 4.0]


def parte_imag(start, stop, lista):
    lista_aux = []
    try:
        for i in range(start, stop):
            lista_aux.append(lista[i].imag)
        return lista_aux
    except IndexError:
        print("Intervalul dat nu se află în listă")
        return -1


def test_modul_mai_mic_ca10():
    lista = [(1+2j), (3+4j), (6+8j)]
    assert modul_mai_mic_ca10(lista) == [(1+2j), (3+4j)]


def modul_mai_mic_ca10(lista):
    lista_aux = []
    for item in lista:
        if abs(item) < 10:
            lista_aux.append(item)
    return lista_aux


def test_modul_egal_cu10():
    lista = [(6+8j), (8+6j), (2+3j), (5+6j)]
    assert modul_egal_cu10(lista) == [(6+8j), (8+6j)]


def modul_egal_cu10(lista):
    lista_aux = []
    for item in lista:
        if abs(item) == 10:
            lista_aux.append(item)
    return lista_aux


def main():
    while True:
        print("Problema 1(Lucru cu numere complexe)")
        print("1.Adaugă număr în listă")
        print("2.Modifică elemente din listă")
        print("3.Căutare numere")
        print("4.Operații cu numerele din listă")
        print("5.Filtrare")
        print("6.Undo")
        print("7.Ieșire")
        p = alegere_optiune()
        if p == 1:
            while True:
                print("1.Adăugare număr complex la final")
                print("2.Adăugare număr complex pe o poziție")
                print("3.Înapoi")
                p = alegere_optiune()
                if p == 1:
                    test_add_la_final()
                    input1 = citire_nr_complex()
                    add_la_final(input1, numere_complexe)
                elif p == 2:
                    test_add_cu_index()
                    index = citire_index()
                    input2 = citire_nr_complex()
                    add_cu_index(input2, index, numere_complexe)
                elif p == 3:
                    break
        elif p == 2:
            while True:
                print("1.Ștergere număr de pe o poziție")
                print("2.Ștergere numere pe un interval")
                print("3.Înlocuirea aparițiilor unui numar cu altul")
                print("4.Înapoi")
                p = alegere_optiune()
                if p == 1:
                    test_stergere_numar()
                    index = citire_index()
                    stergere_numar(index, numere_complexe)
                elif p == 2:
                    test_stergere_interval()
                    start = citire_index()
                    stop = citire_index()
                    stergere_interval(start, stop, numere_complexe)
                elif p == 3:
                    test_inlocuire_numar()
                    inlocuit = citire_nr_complex()
                    inlocuitor = citire_nr_complex()
                    inlocuire_numar(inlocuit, inlocuitor, numere_complexe)
                elif p == 4:
                    break
        elif p == 3:
            while True:
                print("1.Afișare parte imaginară numere dintr-o secvență")
                print("2.Afișare numere cu modulul mai mic decât 10")
                print("3.Afișare numere cu modulul egal cu 10")
                print("4.Înapoi")
                p = alegere_optiune()
                if p == 1:
                    test_parte_imag()
                    start = citire_index()
                    stop = citire_index()
                    print(parte_imag(start, stop, numere_complexe))
                elif p == 2:
                    test_modul_mai_mic_ca10()
                    print(modul_mai_mic_ca10(numere_complexe))
                elif p == 3:
                    test_modul_egal_cu10()
                    print(modul_egal_cu10(numere_complexe))
                elif p == 4:
                    break
        elif p == 4:
            pass
        elif p == 5:
            pass
        elif p == 6:
            pass
        elif p == 7:
            break


main()
