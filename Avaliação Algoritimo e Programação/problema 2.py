n = int(input())
sitios = [int(input()) for _ in range(n)]
print(sum(sitios))
for i in range(n):
  if i == 0:
    if sitios[i] > 0:
      sitios[i]= sitios[i]-1
  elif sitios[i]%2 != 0:
    sitios[i]= sitios[i]-1
    i-1
  else:
    if sitios[i] > 0:
      sitios[i]= sitios[i]-1
      
print(len(sitios),sum(sitios))