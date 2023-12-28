import sys


def bepaal_aantal_nijlpaarden(n_aantal_maaltijden: int, k_sociale_afstand: int) -> int:
    aantal_nijlpaarden = 1
    return aantal_nijlpaarden

def main():
    stdin_fileno = sys.stdin
    
    n_aantal_maaltijden = int(input())
    k_sociale_afstand = int(input())
    
    print(n_aantal_maaltijden)
    print(k_sociale_afstand)

    resultaat = bepaal_aantal_nijlpaarden(n_aantal_maaltijden, k_sociale_afstand)
    print(resultaat)

if __name__ == '__main__':
    main()