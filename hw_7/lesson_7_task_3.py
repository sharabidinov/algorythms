"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой — не больше медианы.

Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод
сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
"""
from random import randint

user_input = int(input('Введите число '))
len_lst = 2 * user_input + 1
array = [randint(1, 100) for _ in range(len_lst)]


def shaker_sort(lst: list):
    first = 0
    last = len(lst)
    while first <= last:

        for idx in range(first, last):
            if lst[idx] > lst[idx] + 1:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
        last -= 1

        for idx in range(last, first, -1):
            if lst[idx - 1] > lst[idx]:
                lst[idx], lst[idx - 1] = lst[idx - 1], lst[idx]
        first += 1

    return lst


def median(lst: list):
    len_ = len(lst)
    return lst[len_ // 2]


print(array)
print(shaker_sort(array))
print(median(array))
