
def bepaal_len_str(s: str)-> int:
    
    if s == '':
        return 0 
    else:
        return 1 + bepaal_len_str(s[1:])

    return 

def main():
    resultaat = bepaal_len_str(input())
    print(resultaat)

if __name__ == '__main__':
    main()
