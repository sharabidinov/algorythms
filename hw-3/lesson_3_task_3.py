# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

lst = [random.randint(1, 100) for i in range(1, 11)]
print(lst)
max_index = 0
min_index = 0

for index in range(len(lst)):
    if lst[index] > lst[max_index]:
        max_index = index
    elif lst[index] < lst[min_index]:
        min_index = index

print(lst[min_index], lst[max_index])
lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
print(lst)
