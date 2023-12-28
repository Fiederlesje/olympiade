def bereken_getal_doel(grondtal_bron: int, getal_bron: str, grondtal_doel: int) -> str:
    getal_decimaal = int(getal_bron, grondtal_bron) 
    loop_getal = getal_decimaal
    getal_doel = ''

    while loop_getal:
        modulus = loop_getal % grondtal_doel
        loop_getal = loop_getal // grondtal_doel
        getal_doel = chr(48 + modulus + 7*(modulus > 10)) + getal_doel

    return getal_doel

def main():
    grondtal_bron = int(input())
    getal_bron = input()
    grondtal_doel = int(input())

    resultaat = bereken_getal_doel(grondtal_bron, getal_bron, grondtal_doel)
    print(resultaat)

if __name__ == '__main__':
    main()

