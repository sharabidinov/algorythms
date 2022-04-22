"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50). Выведите на экран исходный и отсортированный массивы.
"""
from random import uniform, choice

array = [round(uniform(0, 50), 2) for _ in range(20)]


def merge_sort(lst: list):
    if len(lst) <= 1:
        return lst

    item = choice(lst)
    small = []
    equal = []
    big = []

    for itm in lst:
        if itm < item:
            small.append(itm)
        elif itm > item:
            big.append(itm)
        else:
            equal.append(itm)

    return merge_sort(small) + equal + merge_sort(big)


print(merge_sort(array))
