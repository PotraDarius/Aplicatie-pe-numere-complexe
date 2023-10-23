# lista globara de stocare a datelor
numere_complexe = []


# folosit genereal pentru citirea unui numar complex
def citire_nr_complex():
    try:
        real = int(input("Dati partea reala: "))
        imag = int(input("Dati partea imaginara: "))
        return complex(real, imag)
    except ValueError:
        print("Datele nu au fost introduse corect!")


# folosit general pentru citirea unui index pentru navigarea listei generale de date
def citire_index():
    try:
        index = int(input("Dati un index: "))
        return index
    except ValueError:
        print("Datele nu au fost introduse corect!")


# folosit pentru navigarea interfatei
def alegere_optiune():
    try:
        p = int(input("Alege o optiune: "))
        return p
    except ValueError:
        print("Datele nu sunt introduse corect")


def afisare_lista(lista):
    if lista:
        print(lista)
    else:
        print("Lista este goala!")
