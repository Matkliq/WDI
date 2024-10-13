a = int(input('Podaj początek zakresu: '))
b = int(input('Podaj koniec zakresu: '))
if b-a < 20:
    while a<=b:
        print(a)
        a+=1
else:
    sr = (a+b)/2
    print(sr)
    if (a+b)%2:
        for i in range(int(sr)-2,int(sr)+4):
            print(i)
    else:
        for i in range(int(sr)-3,int(sr)+4):
            if i != sr:
                print(i)

