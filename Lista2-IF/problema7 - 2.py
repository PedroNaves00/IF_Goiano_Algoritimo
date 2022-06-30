valor = int(input())
c100 =  c50 =  c20 = c10 = c5 = c2 = c1 = 0
if valor >= 100:
    c100 = valor // 100
    valor = valor - (100*c100)
if valor >= 50:
    c50 = valor // 50
    valor = valor - (50*c50)
if valor >= 20:
    c20 = valor // 20
    valor = valor - (20*c20)
if valor >= 10:
    c10 = valor // 10
    valor = valor - (10*c10)
if valor >= 5:
    c5 = valor // 5
    valor = valor - (5*c5)
if valor >= 2:
    c2 = valor // 2
    valor = valor - (2*c2)
if valor >= 1:
    c1 = valor // 1
    valor = valor - (1*c1)
print(valor)
print(f'{c100} nota (s) de R$ 100,00')
print(f'{c50} nota (s) de R$ 50,00')
print(f'{c20} nota (s) de R$ 20,00')
print(f'{c10} nota (s) de R$ 10,00')
print(f'{c5} nota (s) de R$ 5,00')
print(f'{c2} nota (s) de R$ 2,00')
print(f'{c1} nota (s) de R$ 1,00')




