from errno import ESTALE


tempo = int(input())
segundos = 0
minutos  = 0
horas = 0
if tempo < 60:
    segundos = tempo
else:
    segundos = tempo % 60
if tempo > 60:
    minutos = tempo // 60
if minutos >=60:
    minutos = minutos %60
if tempo >= 3600:
    horas = tempo // 3600
print(f'{horas}:{minutos}:{segundos}')

