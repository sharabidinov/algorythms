# Определить, какое число в массиве встречается чаще всего.
from random import randint

dictionary = {}
lst = [randint(1, 15) for _ in range(100)]
print(lst)

for item in lst:
    if item not in dictionary:
        dictionary[item] = 1
    else:
        dictionary[item] += 1

dict_lst = [(key, value) for key, value in list(dictionary.items())]
print(dict_lst)

num = 0
max_ = 0

for item in dict_lst:
    if item[1] > max_:
        max_ = item[1]
        num = item[0]

print(f'Число {num} встречается чаще всего - {max_} раз/раза')
