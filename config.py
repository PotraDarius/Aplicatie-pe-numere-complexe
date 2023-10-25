import math

# lista globara de stocare a datelor
numere_complexe = []
numere_complexe_pt_undo = []


# folosit genereal pentru citirea unui numar complex
def citire_nr_complex():
    try:
        real = int(input("Dati partea reala: "))
        imag = int(input("Dati partea imaginara: "))
        return real, imag
    except ValueError:
        print("Datele nu au fost introduse corect!")


# functie folosita pentru crearea unui numar complex
# preconditii: real - int
#              imag - int
def creare_nr_complex(real, imag):
    try:
        return int(real), int(imag)
    except ValueError:
        print("Datele nu au fost introduse corect!")


# functie folosita pentru returnarea partii reale a unui numar complex
# preconditii: numar - tuplu de numar complex
# postconditii: partea reala - int
def get_parte_reala(numar):
    return int(numar[0])


# functie folosita pentru returnarea partii imaginare a unui numar complex
# preconditii: numar - tuplu de numar complex
# postconditii: partea imaginara - int
def get_parte_imaginara(numar):
    return int(numar[1])


# functie ce aduna doua numere complexe
# preconditii: numar_1 - tuplu de numar complex
#              numar_2 - tuplu de numar complex
# postconditii: suma - tuplu de numar complex
def suma_numere_complexe(numar_1, numar_2):
    parte_reala_suma = get_parte_reala(numar_1) + get_parte_reala(numar_2)
    parte_imaginara_suma = get_parte_imaginara(numar_1) + get_parte_imaginara(numar_2)
    suma = creare_nr_complex(parte_reala_suma, parte_imaginara_suma)
    return suma


#  functie ce inmulteste doua numere complexe
# preconditii: numar_1 - tuplu de numar complex
#              numar_2 - tuplu de numar complex
# postconditii: produs - tuplu de numar complex
def produs_numere_complexe(numar_1, numar_2):
    parte_reala_produs = get_parte_reala(numar_1)*get_parte_reala(numar_2)
    parte_reala_produs -= get_parte_imaginara(numar_1)*get_parte_imaginara(numar_2)

    parte_imaginara_produs = get_parte_reala(numar_1)*get_parte_imaginara(numar_2)
    parte_imaginara_produs += get_parte_reala(numar_2)*get_parte_imaginara(numar_1)

    produs = creare_nr_complex(parte_reala_produs, parte_imaginara_produs)
    return produs


# functie pentru calcularea modulului unui numar complex
# preconditii: numar - tuplu de numar complex
# postconditii: modul - int
def modul_numar_complex(numar):
    modul = int(math.pow(get_parte_reala(numar), 2))
    modul += int(math.pow(get_parte_imaginara(numar), 2))
    modul = math.isqrt(modul)
    return modul


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


# functia citeste o valoare pentru a fi utilizata
# preconditii: -
# posconditii: -
def citire_valoare():
    try:
        valoare = int(input("Dati o valoare: "))
        return valoare
    except ValueError:
        print("Datele nu au fost introduse corect!")


# functia afiseaza o lista
# preconditii: lista - anytype
# postconditii: -
def afisare_lista(lista):
    if lista:
        print(lista)
    else:
        print("Lista este goala!")
