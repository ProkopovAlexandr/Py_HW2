import random

num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)

print(f'Привет! \nМеня зовут Петя. \nЯ загадал тебе два числа.\nИх произведение равно {num1 * num2}. \nА сумма {num1 + num2}. \nУгадай числа!')
print(num1, num2)
mes1 = int(input('Первое число: '))
mes2 = int(input('Второе число: '))

while mes1 != num1 or mes2 != num2:
    if mes1 == num1 or mes2 == num2:
        print('Ты угадал(а) первое число.')
        while mes2 != num2:
            mes2 = int(input('Второе число: '))
    elif mes2 == num2:
        print('Ты угадал(а) второе число.')
        while mes1 != num1:
            mes1 = int(input('Первое число: '))
    else:
        print('Неверно. Попробуй снова')
        mes1 = int(input('Первое число: '))
        mes2 = int(input('Второе число: '))

print('Ты угадал(а) все числа!!!')