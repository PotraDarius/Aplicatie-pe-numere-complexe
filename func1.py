from config import *


def test_add_la_final():
    lista = [(1, 2), (5, 4)]
    numar = (13, 20)
    assert add_la_final(numar, lista) == [(1, 2), (5, 4), (13, 20)]


# adauga la finalul unei liste un numar complex dat
# ex: lista = [(1, 2), (3, 4)], numar = (5, 6) => lista = [(1, 2), (3, 4), (5, 6)]
def add_la_final(numar, lista):
    undo_list.clear()
    undo_list.extend(lista)
    lista.append(numar)
    return lista


def test_add_cu_index():
    lista = [(3, 4), (7, 8), (5, 9)]
    numar = (14, 17)
    index = 1
    assert add_cu_index(numar, index, lista) == [(3, 4), (14, 17), (7, 8), (5, 9)]


# insereaza un numar complex pe o pozitie data
# ex: lista = [(1, 2), (3, 4), (5, 6)], numar = (7, 8), index = 1 => lista = [(1, 2), (7, 8), (3, 4), (5, 6)]
def add_cu_index(numar, index, lista):
    try:
        undo_list.clear()
        undo_list.extend(lista)
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
