def bereken_minimaal_aantal_stappen(opdracht: str) -> int:
    oost = opdracht.count('O')
    noord = opdracht.count('N')
    zuid = opdracht.count('Z')
    west = opdracht.count('W')

    ver = abs(noord- zuid)
    hor = abs(oost - west)

    minimaal_aantal_stappen = ver + hor

    return minimaal_aantal_stappen

def main():
    k = input()
    opdracht = input()

    resultaat = bereken_minimaal_aantal_stappen(opdracht)
    print(resultaat)

if __name__ == '__main__':
    main()
