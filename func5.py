import config
from config import *
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
    lista = [(2, 6), (8, 9), (3, 5), (9, 3), (1, 2)]
    filtru_parte_reala_prim(lista)
    assert lista == [(8, 9), (9, 3), (1, 2)]


# functia elimina fiecare element din lista une partea reala este un numar prim
# ex: lista = [(2, 6), (8, 9), (3, 5), (9, 3), (1, 2)]
# rezultat: lista = [(8, 9), (9, 3), (1, 2)]
def filtru_parte_reala_prim(lista):
    undo_list.clear()
    undo_list.extend(lista)
    i = 0
    while i < len(lista):
        if este_prim(get_parte_reala(lista[i])) is True:
            del lista[i]
        else:
            i = i+1


def test_filtrare_modul():
    lista = [(6, 8), (8, 6), (2, 3), (5, 6)]
    optiune = 2
    numar = 10
    filtrare_modul(optiune, numar, lista)
    assert lista == [(2, 3), (5, 6)]


# functia elimina fiecare numar complex ce are modulul <, =, > decat un numar dat
# preconditii: optiune - int
#              numar - tuplu de numar complex
#              lista - lista de numere complexe
# postconditii: -
#               lista va fi modificata conform scopului functiei
def filtrare_modul(optiune, numar, lista):
    undo_list.clear()
    undo_list.extend(lista)
    if optiune == 1:
        i = 0
        while i < len(lista):
            if modul_numar_complex(lista[i]) < numar:
                del lista[i]
            else:
                i += 1
    elif optiune == 2:
        i = 0
        while i < len(lista):
            if modul_numar_complex(lista[i]) == numar:
                del lista[i]
            else:
                i += 1
    elif optiune == 3:
        i = 0
        while i < len(lista):
            if modul_numar_complex(lista[i]) > numar:
                del lista[i]
            else:
                i += 1
    else:
        raise ValueError("Optiunea data nu este valabila")


def main():
    while True:
        print("1.Filtrare parte reala prim")
        print("2.Filtrare modul")
        print("3.Înapoi")
        p = alegere_optiune()
        if p == 1:
            filtru_parte_reala_prim(numere_complexe)
        elif p == 2:
            nr = citire_valoare()
            while True:
                print("1.Mai mic (<)")
                print("2.Egal (=)")
                print("3.Mai mare (>)")
                p = alegere_optiune()
                filtrare_modul(p, nr, numere_complexe)
        elif p == 3:
            break
