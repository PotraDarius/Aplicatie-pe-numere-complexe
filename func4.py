from config import *


def test_suma_secventa():
    lista = [(1, 2), (4, 5), (7, 8), (6, 9), (15, 16)]
    start = 0
    stop = 3
    assert suma_secventa(start, stop, lista) == (12, 15)


# calculeaza si returneaza suma numerelor dintr-o secventa data din lista
# ex: lista = lista = [(1, 2), (4, 5), (7, 8), (6, 9), (15, 16)] , start = 0, stop = 3
# output: (12, 15)
def suma_secventa(start, stop, lista):
    undo_list.clear()
    undo_list.extend(lista)
    try:
        suma = (0, 0)
        for i in range(start, stop):
            suma = suma_numere_complexe(suma, lista[i])
        return suma
    except IndexError:
        print("Secventa data nu exista in lista!")


def test_produs_secventa():
    lista = [(1, 2), (4, 5), (7, 8), (6, 9), (15, 16)]
    start = 0
    stop = 3
    assert produs_secventa(start, stop, lista) == (-146, 43)


# calculeaza si returneaza produsul numerelor dintr-o secventa data din lista
# ex: lista = lista = [(1, 2), (4, 5), (7, 8), (6, 9), (15, 16)] , start = 0, stop = 3
# output: (-146, 43)
def produs_secventa(start, stop, lista):
    undo_list.clear()
    undo_list.extend(lista)
    try:
        produs = (lista[start])
        for i in range(start+1, stop):
            produs = produs_numere_complexe(produs, lista[i])
        return produs
    except IndexError:
        print("Secventa data nu exista in lista!")


def test_afisare_descrescatoare():
    lista = [(1, 2), (4, 5), (7, 8), (6, 9), (15, 16)]
    assert afisare_descrescatoare(lista) == [(15, 16), (6, 9), (7, 8), (4, 5), (1, 2)]


# afiseaza o lista in mod descrescator dupa partea imaginara a numerelor, fara a modifica lista
# ex: input: lista = [(1, 2), (4, 5), (7, 8), (6, 9), (15, 16)]:
#     output: [(15, 16), (6, 9), (7, 8), (4, 5), (1, 2)]
def afisare_descrescatoare(lista):
    return sorted(lista, key=lambda x: get_parte_imaginara(x), reverse=True)


def main():
    while True:
        print("1.Suma numerelor dintr-o subsecventă dată")
        print("2.Produsul numerelor dintr-o subsecventă dată")
        print("3.Tipărește lista sortată descrescător după partea imaginară")
        print("4.Înapoi")
        p = alegere_optiune()
        if p == 1:
            start = citire_index()
            stop = citire_index()
            print("Lista: " + str(numere_complexe[start:stop]))
            text = suma_secventa(start, stop, numere_complexe)
            print("Suma: " + str(text))
        elif p == 2:
            start = citire_index()
            stop = citire_index()
            print("Lista: " + str(numere_complexe[start:stop]))
            text = produs_secventa(start, stop, numere_complexe)
            print("Suma: " + str(text))
        elif p == 3:
            print(afisare_descrescatoare(numere_complexe))
        elif p == 4:
            break
