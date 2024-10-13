a=int(input('Podaj 1 liczbę: '))
b=int(input('Podaj 2 liczbę: '))
if a < 0 and b<0:
    exit("Obydwie liczby są mniejsze od 0")
if a<0:
    a=-a
if b<0:
    b=-b
print('Suma wynosi',a+b)
print('Różnica wynosi',a-b)
print('Iloczyn wynosi',a*b)
if a*b==10:
    print('Yay!')
if b==0:
    print("Nie można dzielić przez 0")
else:
    print('Iloraz wynosi ', a/b)
print('Kwadrat 1 liczby wynosi',a**2)
print('Kwadrat 2 liczby wynosi',b**2)
print('Pierwiastek 1 liczby wynosi',a**(1/2))
print('Pierwiastek 2 liczby wynosi',b**(1/2))
