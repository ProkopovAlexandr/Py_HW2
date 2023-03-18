import random

arr_nums = []
for i in range(3):
    arr_nums.append(random.randint(0, 999))
print(arr_nums)
print(''.join((sorted([str(x) for x in arr_nums], reverse=True))))