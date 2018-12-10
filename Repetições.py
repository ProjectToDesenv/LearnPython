cont = 1
while cont <= 10:
    print(cont)
    cont += 1

cont = 1
while cont <= 100:
    if cont % 2 == 0:
        print(cont, end= '')
    cont += 1

tabuada = 1
while tabuada <=10:
    numero = 1
    while numero <= 10:
        print('%d X %d = %d' % (tabuada,numero,tabuada * numero))
        numero += 1
    tabuada += 1    