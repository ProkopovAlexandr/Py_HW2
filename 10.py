import random
n_coins = int(input("Введите кол-во монет: "))
coins_pos = []
i = 0
resh = 0
gerb = 0

for i in range(n_coins):
    coins_pos.append(random.randint(0, 1))
    if coins_pos[i] == 0:
        resh += 1
    else:
        gerb += 1

print("Монеты:", coins_pos)

if resh > gerb:
    print("Нужно перевернуть минимум ", gerb, " монет.")
elif resh < gerb:
    print("Нужно перевернуть минимум ", resh, " монет.")
else:
    print("Нужно перевернуть половину всех монет.")