def problema1():
    n =  al = ga = disel = 0
    while n != 4:
        n = int(input())
        if n == 1:
            al += 1
        elif n == 2:
            ga += 1
        elif n == 3:
            disel += 1
        elif n == 4:
            break
    print('MUITO OBRIGADO')
    print(f'Alcool: {al} ')
    print(f'Gasolina: {ga}')
    print(f'Disel: {disel}')
problema1()
