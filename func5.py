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
    lista = [(2, 6), (8, 9), (3, 5), (9, 3), (1, 2)]
    assert filtru_parte_reala_prim(lista) == [(8, 9), (9, 3), (1, 2)]


# functia elimina fiecare element din lista une partea reala este un numar prim
# ex: lista = [(2, 6), (8, 9), (3, 5), (9, 3), (1, 2)]
# rezultat: lista = [(8, 9), (9, 3), (1, 2)]
def filtru_parte_reala_prim(lista):
    i = 0
    while i < len(lista):
        if este_prim(config.get_parte_reala(lista[i])) is True:
            del lista[i]
        else:
            i = i+1
    return lista


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
    if optiune == 1:
        i = 0
        while i < len(lista):
            if config.modul_numar_complex(lista[i]) < numar:
                del lista[i]
            else:
                i += 1
    elif optiune == 2:
        i = 0
        while i < len(lista):
            if config.modul_numar_complex(lista[i]) == numar:
                del lista[i]
            else:
                i += 1
    elif optiune == 3:
        i = 0
        while i < len(lista):
            if config.modul_numar_complex(lista[i]) > numar:
                del lista[i]
            else:
                i += 1


def main():
    while True:
        print("1.Filtrare parte reala prim")
        print("2.Filtrare modul")
        print("3.Înapoi")
        p = config.alegere_optiune()
        if p == 1:
            filtru_parte_reala_prim(config.numere_complexe)
        elif p == 2:
            nr = config.citire_valoare()
            while True:
                print("1.Mai mic (<)")
                print("2.Egal (=)")
                print("3.Mai mare (>)")
                p = config.alegere_optiune()
                filtrare_modul(p, nr, config.numere_complexe)
        elif p == 3:
            break
