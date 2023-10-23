import func1
import func2
import func3
import func4
import func5
import func6
from func1 import *
from func2 import *
from func3 import *
from func4 import *
from func5 import *
from func6 import *


def main():
    while True:
        print("Problema 1(Lucru cu numere complexe)")
        print("1.Adaugă număr în listă")
        print("2.Modifică elemente din listă")
        print("3.Căutare numere")
        print("4.Operații cu numerele din listă")
        print("5.Filtrare")
        print("6.Undo")
        print("7.Afișare listă")
        print("8.Ieșire")
        p = alegere_optiune()
        if p == 1:
            func1.main()
        elif p == 2:
            func2.main()
        elif p == 3:
            func3.main()
        elif p == 4:
            func4.main()
        elif p == 5:
            func5.main()
        elif p == 6:
            func6.main()
        elif p == 7:
            afisare_lista(numere_complexe)
        elif p == 8:
            break


test_add_la_final()
test_stergere_numar()
test_stergere_interval()
test_inlocuire_numar()
test_parte_imag()
test_modul_mai_mic_ca10()
test_modul_egal_cu10()
test_prim()
test_filtru_parte_reala_prim()
test_suma_secventa()
test_produs_secventa()
test_afisare_descrescatoare()
main()
