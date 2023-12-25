
def meest_voorkomende_letters(input_tekst: str) -> str:
    letterteller = {}
    max_aantal_letters = 0
    set_unieke_letters = set(input_tekst)

    for letter in set_unieke_letters:
        letterteller[letter] = input_tekst.count(letter)
        if letterteller[letter] > max_aantal_letters:
            max_aantal_letters = letterteller[letter]
    
    lijst_meest_voorkomende_letters = sorted([k for k, v in letterteller.items() if v == max_aantal_letters])
    meest_voorkomende_letters = ''.join(lijst_meest_voorkomende_letters)
    
    return meest_voorkomende_letters

def main():
    input_tekst = input()

    resultaat = meest_voorkomende_letters(input_tekst)
    print(resultaat)

if __name__ == '__main__':
    main()
