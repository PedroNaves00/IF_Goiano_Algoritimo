from ast import For
from cmath import pi


x = int(input())
v = []
i = 0
v.insert(0, x)
for i in range(0, 10):
    x *= 2
    v.append(x)
    print(f'N[{i}] = {v[i]}')
    
    
    


    











