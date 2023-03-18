max = int(input('Введите максимальное число: '))
i = 0
while 2**i <= max:
    print(2**i, end=' ')
    i += 1
