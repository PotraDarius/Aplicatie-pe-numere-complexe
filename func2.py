import config


def test_stergere_numar():
    lista = [(3+4j), (5+7j), (9+8j), (14+15j)]
    index = 2
    assert stergere_numar(index, lista) == [(3+4j), (5+7j), (14+15j)]


# sterge un numar din lista de pe o pizitie data
# ex: lista = [(1+2j), (7+8j), (45+78j), (3+6j)], index = 2 => lista = [(1+2j), (7+8j), (3+6j)]
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


# stergele elementele dintr-un interval dat din lista
# ex: lista = [(1+2j), (3+4j), (5+6j), (7+8j), (4+10j)], start = 1, stop = 4 =>
# => lista = [(1+2j), (4+10j)]
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


# inlocuieste fiecare aparitie a unui numar cu un alt numar intr-o lista
# ex: lista = [(1+2j), (5+7j), (1+2j), (24+13j), (1+2j)]
#     inlocuitor = (3+4j)
#     inlocuit = (1+2j)
# rezultat: [(3+4j), (5+7j), (3+4j), (24+13j), (3+4j)]
def inlocuire_numar(inlocuit, inlocuitor, lista):
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
        p = config.alegere_optiune()
        if p == 1:
            index = config.citire_index()
            stergere_numar(index, config.numere_complexe)
        elif p == 2:
            start = config.citire_index()
            stop = config.citire_index()
            stergere_interval(start, stop, config.numere_complexe)
        elif p == 3:
            inlocuit = config.citire_nr_complex()
            inlocuitor = config.citire_nr_complex()
            inlocuire_numar(inlocuit, inlocuitor, config.numere_complexe)
        elif p == 4:
            break
