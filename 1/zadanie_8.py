n = int(input('Podaj wysokość: '))
for i in range(1, n+1):
    wiersz = ''
    for j in range(n-i):
        wiersz += ' '
    if i != 1:
        for j in range(1, 2*i):
            if (j+i)%3 !=0:
                wiersz += '*'
            else:
                wiersz += 'o'
    else:
        wiersz += 'X'
    print(wiersz)
wiersz = ''
for i in range(n-1):
    wiersz += ' '
wiersz += 'U'
print(wiersz)