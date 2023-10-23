from config import *


def test_add_la_final():
    lista = [(1+2j), (5+4j)]
    numar = (13+20j)
    assert add_la_final(numar, lista) == [(1+2j), (5+4j), (13+20j)]


# adauga la finalul unei liste un numar complex dat
# ex: lista = [(1+2j), (3+4j)], numar = (5+6j) => lista = [(1+2j), (3+4j), (5+6j)]
def add_la_final(numar, lista):
    lista.append(numar)
    return lista


def test_add_cu_index():
    lista = [(3+4j), (7+8j), (5+9j)]
    numar = (14+17j)
    index = 1
    assert add_cu_index(numar, index, lista) == [(3+4j), (14+17j), (7+8j), (5+9j)]


# insereaza un numar complex pe o pozitie data
# ex: lista = [(1+2j), (3+4j), (5+6j)], numar = (7+8j), index = 1 => lista = [(1+2j), (7+8j), (3+4j), (5+6j)]
def add_cu_index(numar, index, lista):
    try:
        lista.insert(index, numar)
        return lista
    except IndexError:
        print("Nu s-a gasit indexul dat")
        return -1


def main():
    while True:
        print("1.Adăugare număr complex la final")
        print("2.Adăugare număr complex pe o poziție")
        print("3.Înapoi")
        p = alegere_optiune()
        if p == 1:
            input1 = citire_nr_complex()
            add_la_final(input1, numere_complexe)
        elif p == 2:
            test_add_cu_index()
            index = citire_index()
            input2 = citire_nr_complex()
            add_cu_index(input2, index, numere_complexe)
        elif p == 3:
            break
