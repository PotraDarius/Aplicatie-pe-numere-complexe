from config import *
from func5 import filtru_parte_reala_prim


def test_undo():
    lista = [(2, 6), (8, 9), (3, 5), (9, 3), (1, 2)]
    filtru_parte_reala_prim(lista)
    undo(lista)
    assert lista == [(2, 6), (8, 9), (3, 5), (9, 3), (1, 2)]
    undo_list.clear()


# functia readuce lista data la ultima valoare inainte de efectuarea ultimei operatii pe ea, folosindu-se de lista_undo
# preconditii: lista_undo - nevida
# postconditii: -
#               lista este readuca la o valoare anterioara
def undo(lista):
    if undo_list or (not undo_list and lista):
        lista.clear()
        lista.extend(undo_list)
    else:
        raise ValueError("Nu s-a efectuat o operatie pana acuma")


def main():
    while True:
        print("1.Undo")
        p = alegere_optiune()
        if p == 1:
            undo(numere_complexe)
            break
