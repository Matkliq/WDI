import os
import random
import math

def header(n):
    os.system('cls' if os.name == 'nt' else 'clear')
    napis = ''
    for i in range(n*2):
        napis += '=-'
    napis += '\n'
    for i in range(n):
        napis += ' '
    napis += 'Kalkulator\n'
    for i in range(n*2):
        napis += '=-'
    print(napis)


def kalkulator():
    header(10)
    a = int(input('Podaj 1 liczbę: '))
    b = int(input('Podaj 2 liczbę: '))
    c = input('Wybierz działanie (+, -, *, /, #, ^, x): ')
    if  c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '*':
        print(a*b)
    elif c == '/':
        print(a/b)
    elif c == '^':
        print(a**b)
    elif c == '#':
        print(math.log(a, b))
    elif c == 'x':
        print(random.randint(a,b))
    else:
        print('Nienzane działanie '+c)
    r = input('Czy chcesz wprowadzić nowe dane? (T/N): ')
    if r == 'T' or r == 't':
        kalkulator()
    else:
        exit()
kalkulator()