import config


def test_parte_imag():
    lista = [(1 + 2j), (3 + 4j), (7 + 8j)]
    assert parte_imag(0, 2, lista) == [2.0, 4.0]


# afiseaza partea imaginara a fiecarui numar dintr-o secventa dintr-o lista
# ex: lista = [(1+2j), (3+4j), (7+8j)], start = 0, stop = 2
# output: [2.0, 4.0]
def parte_imag(start, stop, lista):
    lista_aux = []
    try:
        for i in range(start, stop):
            lista_aux.append(lista[i].imag)
        return lista_aux
    except IndexError:
        print("Intervalul dat nu se află în listă")
        return -1


def test_modul_mai_mic_ca10():
    lista = [(1 + 2j), (3 + 4j), (6 + 8j)]
    assert modul_mai_mic_ca10(lista) == [(1 + 2j), (3 + 4j)]


# afiseaza fiecare numar complex a carui modul e mai mic ca 10 din lista
# ex: lista = [(1+2j), (3+4j), (6+8j)]
# output: [(1+2j), (3+4j)]
def modul_mai_mic_ca10(lista):
    lista_aux = []
    for item in lista:
        if abs(item) < 10:
            lista_aux.append(item)
    return lista_aux


def test_modul_egal_cu10():
    lista = [(6 + 8j), (8 + 6j), (2 + 3j), (5 + 6j)]
    assert modul_egal_cu10(lista) == [(6 + 8j), (8 + 6j)]


# afiseaza fiecare numar complex a carui modul este egal cu 10 din lista
# ex: lista = [(6+8j), (8+6j), (2+3j), (5+6j)]
# output: [(6+8j), (8+6j)]
def modul_egal_cu10(lista):
    lista_aux = []
    for item in lista:
        if abs(item) == 10:
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
