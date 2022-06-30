tempo = int(input())
ano = 0 
mes = 0
dia = 0
if tempo < 30:
    dia = tempo
elif tempo >= 30:
    mes = tempo // 30
    ano = tempo // 365 
    dia = tempo - (ano * 365 + mes * 30)
    if mes >= 12:
        mes = mes % 12
        dia = tempo - (ano * 365 + mes * 30)
print(f'{ano} ano (s)') 
print(f'{mes} mes (es)')
print(f'{dia} dia (s)')
