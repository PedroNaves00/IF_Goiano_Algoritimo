def problema6():
    par = []
    impar = []
    valor = 0
    x = 0
    w = 0
    z = 0
    o = (len(par) - z)
    for c in range(0, 15):
        valor = int(input())
        if valor % 2 == 0:
            par.append(valor)
        else:
            impar.append(valor)
    for i in par:
        if x < 5:
            x += 1
            print(f'par[{x-1}] = {i}')
    for y in impar:
        w += 1
        print(f'impar[{w-1}] = {y}')
    print(par)
    for p in par:
        z += 1
        while o > 5:
            print(f'par[{z-1}] = {par[len(par)-z]}')
        else:
            break
problema6()
    
        
            