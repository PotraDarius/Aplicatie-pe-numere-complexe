import config
import math


# functia returneaza True daca numarul dat este prim si False in caz contrat
# ex: input: 3 output: True
# ex: input: 6 output: False
def test_prim():
    assert este_prim(1) is False
    assert este_prim(2) is True
    assert este_prim(8) is False
    assert este_prim(3) is True
    assert este_prim(9) is False


def este_prim(numar):
    if numar <= 1:
        return False
    if numar != 2 and numar % 2 == 0:
        return False
    for i in range(2, math.isqrt(numar)+1):
        if numar % i == 0:
            return False
    return True


def test_filtru_parte_reala_prim():
    lista = [(2+6j), (8+9j), (3+5j), (9+3j), (1+2j)]
    assert filtru_parte_reala_prim(lista) == [(8+9j), (9+3j), (1+2j)]


# functia elimina fiecare element din lista une partea reala este un numar prim
# ex: lista = [(2+6j), (8+9j), (3+5j), (9+3j), (1+2j)]
# rezultat: lista = [(8+9j), (9+3j), (1+2j)]
def filtru_parte_reala_prim(lista):
    i = 0
    while i < len(lista):
        if este_prim(int(lista[i].real)) is True:
            del lista[i]
        else:
            i = i+1
    return lista


def main():
    while True:
        print("1.Filtrare parte reala prim")
        print("2.Filtrare modul")
        print("3.Înapoi")
        p = config.alegere_optiune()
        if p == 1:
            filtru_parte_reala_prim(config.numere_complexe)
        elif p == 2:
            pass
        elif p == 3:
            break
