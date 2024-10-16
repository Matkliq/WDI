def pierwsza(n):
    if n == 2:
        return True
    i = 2
    if n<2 or n%2 == 0:
        return False
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
n = int(input('Podaj liczbę: '))
if pierwsza(n):
    print('Liczba',n,'jest pierwsza')
else:
    print('Liczba',n,'nie jest pierwsza')