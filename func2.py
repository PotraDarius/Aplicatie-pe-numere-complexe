from config import *


def test_stergere_numar():
    lista = [(3, 4), (5, 7), (9, 8), (14, 15)]
    index = 2
    assert stergere_numar(index, lista) == [(3, 4), (5, 7), (14, 15)]


# sterge un numar din lista de pe o pizitie data
# ex: lista = [(1, 2), (7, 8), (45, 78), (3, 6)], index = 2 => lista = [(1, 2), (7, 8), (3, 6)]
def stergere_numar(index, lista):
    try:
        undo_list.clear()
        undo_list.extend(lista)
        del lista[index]
        return lista
    except IndexError:
        print("Nu există un număr pe această poziție!")
        return -1


def test_stergere_interval():
    lista = [(1, 2), (3, 4), (5, 6), (7, 8), (4, 10)]
    start = 1
    stop = 4
    assert stergere_interval(start, stop, lista) == [(1, 2), (4, 10)]


# stergele elementele dintr-un interval dat din lista
# ex: lista = [(1, 2), (3, 4), (5, 6), (7, 8), (4, 10)], start = 1, stop = 4 =>
# => lista = [(1, 2), (4, 10)]
def stergere_interval(start, stop, lista):
    try:
        undo_list.clear()
        undo_list.extend(lista)
        del lista[start:stop]
        return lista
    except IndexError:
        print("Intervalul dat nu există în listă")
        return -1


def test_inlocuire_numar():
    lista = [(1, 2), (5, 7), (1, 2), (24, 13), (1, 2)]
    inlocuitor = (3, 4)
    inlocuit = (1, 2)
    assert inlocuire_numar(inlocuit, inlocuitor, lista) == [0, 2, 4]


# inlocuieste fiecare aparitie a unui numar cu un alt numar intr-o lista
# ex: lista = [(1, 2), (5, 7), (1, 2), (24, 13), (1, 2)]
#     inlocuitor = (3, 4)
#     inlocuit = (1, 2)
# rezultat: [(3, 4), (5, 7), (3, 4), (24, 13), (3, 4)]
def inlocuire_numar(inlocuit, inlocuitor, lista):
    undo_list.clear()
    undo_list.extend(lista)
    lista_aux = []
    for i in range(0, len(lista)):
        if lista[i] == inlocuit:
            lista[i] = inlocuitor
            lista_aux.append(i)
    return lista_aux


def main():
    while True:
        print("1.Ștergere număr de pe o poziție")
        print("2.Ștergere numere pe un interval")
        print("3.Înlocuirea aparițiilor unui numar cu altul")
        print("4.Înapoi")
        p = alegere_optiune()
        if p == 1:
            index = citire_index()
            stergere_numar(index, numere_complexe)
        elif p == 2:
            start = citire_index()
            stop = citire_index()
            stergere_interval(start, stop, numere_complexe)
        elif p == 3:
            inlocuit = citire_nr_complex()
            inlocuitor = citire_nr_complex()
            inlocuire_numar(inlocuit, inlocuitor, numere_complexe)
        elif p == 4:
            break
