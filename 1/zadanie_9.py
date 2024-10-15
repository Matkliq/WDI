import os
def menu(saldo):
    os.system('cls' if os.name == 'nt' else 'clear')
    komunikat = 'Co chcesz zrobić w kolejnym kroku? \n 1. Wpłata \n 2. Wypłata \n 3. Saldo \n 4. Wyjście\n'
    a = int(input(komunikat))
    if a == 1:
        if pin():
            wplata = int(input('Podaj ile chcesz wpłacić: '))
            saldo += wplata
            print('\nWplacono',wplata,'zł. Twoje aktualne saldo wynosi',saldo,'zł.')
            input("\nKliknij enter aby wrócić do menu")
            menu(saldo)
    if a == 2:
        if pin():
            wyplata = int(input('Podaj ile chcesz wyplacić: '))
            if wyplata < saldo:
                saldo -= wyplata
                print('\nWyplacono',wyplata,'zł. Twoje aktualne saldo wynosi',saldo,'zł.')
                input("\nKliknij enter aby wrócić do menu")
                menu(saldo)
            else:
                print('\nNie masz tyle pieniędzy na koncie.')
                input("\nKliknij enter aby wrócić do menu")
                menu(saldo)

    if a == 3:
        if pin():
            print('\nTwoje saldo wynosi: ', saldo)
            input("\nKliknij enter aby wrócić do menu")
            menu(saldo)
    else:
        exit()

def pin():
    b = input("Podaj kod PIN: \t")
    if b == '1234':
        return True
    else:
        print('\nBłędny kod PIN')
        input("\nKliknij enter aby wrócić do menu")
        menu(saldo)
        return False
saldo = 0
menu(saldo)
