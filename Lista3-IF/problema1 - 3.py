def problema1(n):
    d = 0
    f = 0 
    for x in range(n):
        x = int(input())
        if 10<=x<=20:
            d += 1
        else:
            f += 1
    
    return d, f

n = int(input())
d,f = problema1(n) 

print(f'{d} dentro')
print(f'{f} fora')



