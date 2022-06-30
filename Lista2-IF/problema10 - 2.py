valor = float(input())
#notas
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
#modeas
m1 = m05 = m025 =  m010 = m005 = m001 = 0
if valor >= 1:
    m1 = valor // 1
    valor = valor - (1*m1)
if valor >= 0.5:
    m05 = valor // 0.5
    valor = valor - (0.5*m05)
if valor >= 0.25:
    m025 = valor // 0.25
    valor = valor - (0.25*m025)
if valor >= 0.10:
    m010 = valor // 0.10
    valor = valor - (0.10*m010)
if valor >= 0.05:
    m005 = valor // 0.05
    valor = valor - (0.05*m005)
if valor >= 0.01:
    m001 = valor // 0.01
    valor = valor - (0.01*m001)
print('Notas:')
print(f'{c100} nota (s) de R$ 100,00')
print(f'{c50} nota (s) de R$ 50,00')
print(f'{c20} nota (s) de R$ 20,00')
print(f'{c10} nota (s) de R$ 10,00')
print(f'{c5} nota (s) de R$ 5,00')
print(f'{c2} nota (s) de R$ 2,00')
print('MOEDAS:')
print(f'{m1} moeda (s) de R$ 1.00')
print(f'{m05} moeda (s) de R$ 0.50')
print(f'{m025} moeda (s) de R$ 0.25')
print(f'{m010} moeda (s) de R$ 0.10')
print(f'{m005} moeda (s) de R$ 0.05')
print(f'{m001} moeda (s) de R$ 0.01')



