from config import *


def test_suma_secventa():
    lista = [(1+2j), (4+5j), (7+8j), (6+9j), (15+16j)]
    start = 0
    stop = 3
    assert suma_secventa(start, stop, lista) == (12+15j)


# calculeaza si returneaza suma numerelor dintr-o secventa data din lista
# ex: lista = lista = [(1+2j), (4+5j), (7+8j), (6+9j), (15+16j)] , start = 0, stop = 3
# output: (12+15j)
def suma_secventa(start, stop, lista):
    try:
        suma = 0
        for i in range(start, stop):
            suma += lista[i]
        return suma
    except IndexError:
        print("Secventa data nu exista in lista!")


def test_produs_secventa():
    lista = [(1+2j), (4+5j), (7+8j), (6+9j), (15+16j)]
    start = 0
    stop = 3
    assert produs_secventa(start, stop, lista) == (-146+43j)


# calculeaza si returneaza produsul numerelor dintr-o secventa data din lista
# ex: lista = lista = [(1+2j), (4+5j), (7+8j), (6+9j), (15+16j)] , start = 0, stop = 3
# output: (-146+43j)
def produs_secventa(start, stop, lista):
    try:
        produs = 1
        for i in range(start, stop):
            produs *= lista[i]
        return produs
    except IndexError:
        print("Secventa data nu exista in lista!")


def test_afisare_descrescatoare():
    lista = [(1+2j), (4+5j), (7+8j), (6+9j), (15+16j)]
    assert afisare_descrescatoare(lista) == [(15+16j), (6+9j), (7+8j), (4+5j), (1+2j)]


# afiseaza o lista in mod descrescator dupa partea imaginara a numerelor, fara a modifica lista
# ex: input: lista = [(1+2j), (4+5j), (7+8j), (6+9j), (15+16j)]:
#     output: [(15+16j), (6+9j), (7+8j), (4+5j), (1+2j)]
def afisare_descrescatoare(lista):
    return sorted(lista, key=lambda x: x.imag, reverse=True)


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
