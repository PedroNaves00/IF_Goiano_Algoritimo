def problema2(x, qtd):
    for c in range(qtd):
        matriz = int(input())
        if matriz <= 0:
            x.insert(c, 1)
        else:
            x.insert(c, matriz)

        print(f'X[{c}] = {matriz[c]}')
    
    return x


x = []
qtd = int(input())
X = problema2(x, qtd)










