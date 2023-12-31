def bereken_getal_decimaal(grondtal_bron: int, getal_bron: str)-> int:
    getal_decimaal = int(getal_bron, grondtal_bron) 
 
    return getal_decimaal

def maak_letters(modulus: int)-> str:
    if modulus < 10:
        return str(modulus)
    else:
        return chr(modulus + 87)
    

def bereken_getal_doel(getal_decimaal: int, grondtal_doel: int) -> list:
    modulus = getal_decimaal % grondtal_doel
    floor_divide = getal_decimaal // grondtal_doel

    if floor_divide == 0:
        return str(modulus)
    else:
        return bereken_getal_doel(floor_divide, grondtal_doel) + maak_letters(modulus)
    

def main():
    grondtal_bron = int(input())
    getal_bron = input()
    grondtal_doel = int(input())

    getal_decimaal = bereken_getal_decimaal(grondtal_bron, getal_bron)
    resultaat = bereken_getal_doel(getal_decimaal, grondtal_doel)

    print(resultaat)


if __name__ == '__main__':
    main()