def problema4():
    n = media = total = 0
    list = []
    while n >= 0:
        n = int(input())
        if n >=0:
            list.append(n)
            total += n
        else:
            break
    media = total / len(list)
    print(f'{media:.2f}')
problema4()