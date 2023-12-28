import sys


def bepaal_aantal_nijlpaarden(set_maaltijden: set, k_sociale_afstand: int) -> int:
    maaltijd_invloedsfeer_lege_plekken = []
    maaltijdteller = {}
    min_aantal_invloedsfeer = len(set_maaltijden)
    nijlpaard_seating = []

    for maaltijd in set_maaltijden:
        for plaats in range(1, 1+k_sociale_afstand):
            maaltijd_invloedsfeer_lege_plekken.append(maaltijd - plaats)
            maaltijd_invloedsfeer_lege_plekken.append(maaltijd)
            maaltijd_invloedsfeer_lege_plekken.append(maaltijd + plaats)

    maaltijd_invloedsfeer = [x for x in maaltijd_invloedsfeer_lege_plekken if x in set_maaltijden]
    print(maaltijd_invloedsfeer_lege_plekken)
    print(maaltijd_invloedsfeer)

    for maaltijd in set_maaltijden:
        maaltijdteller[maaltijd] = maaltijd_invloedsfeer.count(maaltijd)
        if maaltijdteller[maaltijd] < min_aantal_invloedsfeer:
            min_aantal_invloedsfeer = maaltijdteller[maaltijd]

    lijst_minst_voorkomende_maaltijden = sorted([k for k, v in maaltijdteller.items() if v == min_aantal_invloedsfeer])
    print(lijst_minst_voorkomende_maaltijden)

    nijlpaard_seating.append(lijst_minst_voorkomende_maaltijden[:1])
    print(nijlpaard_seating)

    # lijst naar int
    # invloedsfeer eerste seating uit lijst halen
    # loop opnieuw tot lijst op is
    
    aantal_nijlpaarden = 100
    return aantal_nijlpaarden

def main():    
    # n_aantal_maaltijden = int(input())
    # k_sociale_afstand = int(input())
    n_aantal_maaltijden = 4
    k_sociale_afstand = 2
    lijst_maaltijden = [1,2,2,4]
    set_maaltijden = set(lijst_maaltijden)
    print(k_sociale_afstand)
    print(set_maaltijden)


    resultaat = bepaal_aantal_nijlpaarden(set_maaltijden, k_sociale_afstand)
    print(resultaat)

if __name__ == '__main__':
    main()