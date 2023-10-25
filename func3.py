import config


def test_parte_imag():
    lista = [(1, 2), (3, 4), (7, 8)]
    assert parte_imag(0, 2, lista) == [2, 4]


# afiseaza partea imaginara a fiecarui numar dintr-o secventa dintr-o lista
# ex: lista = [(1, 2), (3, 4), (7, 8)], start = 0, stop = 2
# output: [2, 4]
def parte_imag(start, stop, lista):
    lista_aux = []
    try:
        for i in range(start, stop):
            lista_aux.append(lista[i][1])
        return lista_aux
    except IndexError:
        print("Intervalul dat nu se află în listă")
        return -1


def test_modul_mai_mic_ca10():
    lista = [(1, 2), (3, 4), (6, 8)]
    assert modul_mai_mic_ca10(lista) == [(1, 2), (3, 4)]


# afiseaza fiecare numar complex a carui modul e mai mic ca 10 din lista
# ex: lista = [(1, 2), (3, 4), (6, 8)]
# output: [(1, 2), (3, 4)]
def modul_mai_mic_ca10(lista):
    lista_aux = []
    for item in lista:
        if config.modul_numar_complex(item) < 10:
            lista_aux.append(item)
    return lista_aux


def test_modul_egal_cu10():
    lista = [(6, 8), (8, 6), (2, 3), (5, 6)]
    assert modul_egal_cu10(lista) == [(6, 8), (8, 6)]


# afiseaza fiecare numar complex a carui modul este egal cu 10 din lista
# ex: lista = [(6, 8), (8, 6), (2, 3), (5, 6)]
# output: [(6, 8), (8, 6)]
def modul_egal_cu10(lista):
    lista_aux = []
    for item in lista:
        if config.modul_numar_complex(item) == 10:
            lista_aux.append(item)
    return lista_aux


def main():
    while True:
        print("1.Afișare parte imaginară numere dintr-o secvență")
        print("2.Afișare numere cu modulul mai mic decât 10")
        print("3.Afișare numere cu modulul egal cu 10")
        print("4.Înapoi")
        p = config.alegere_optiune()
        if p == 1:
            start = config.citire_index()
            stop = config.citire_index()
            print(parte_imag(start, stop, config.numere_complexe))
        elif p == 2:
            print(modul_mai_mic_ca10(config.numere_complexe))
        elif p == 3:
            print(modul_egal_cu10(config.numere_complexe))
        elif p == 4:
            break
