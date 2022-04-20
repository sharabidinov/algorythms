"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти. Примечание:
По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:

● выбрать хорошую задачу, которую имеет смысл оценивать по памяти (укажите какую задачу вы взяли в комментарии);

● написать 3 варианта кода (один у вас уже есть);

● проанализировать 3 варианта и выбрать оптимальный;

● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с
кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;

● написать общий вывод: какой из трёх вариантов лучше и почему.

Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной, а проявили
творчество, фантазию и создали универсальный код для замера памяти.
"""

# 4-я задача 3-го урока
# Определить, какое число в массиве встречается чаще всего.
# Ubuntu 20.04 LTS 64 bit
from sys import getsizeof
from random import randint

dictionary = {}
FUNC_SIZE = 136

# lst_1 = [randint(1, 15) for _ in range(1000)]
lst_2 = [randint(1, 15) for _ in range(10_000)]


def count_max_1(lst: list):
    print('*' * 95)
    print('Вычисляем сколько памяти занимает count_max_1')
    for item in lst:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    dict_lst = [(key, value) for key, value in list(dictionary.items())]

    num = 0
    max_ = 0

    for item in dict_lst:
        if item[1] > max_:
            max_ = item[1]
            num = item[0]

    dict_size = getsizeof(dictionary)
    lst_size = getsizeof(lst)
    dict_lst_size = getsizeof(dict_lst)
    num_size = getsizeof(num)
    max_size = getsizeof(max_)
    print(f'dict_size - {dict_size} байт')
    print(f'lst_size - {lst_size} байт')
    print(f'dict_lst_size - {dict_lst_size} байт')
    print(f'num_size - {num_size} байт')
    print(f'max_size - {max_size} байт')
    # return f'count_max_1 занимает {sum([lst_size, dict_size, dict_lst_size, num_size, max_size, FUNC_SIZE])} байт'
    return f'count_max_1 занимает {sum([dict_size, dict_lst_size, num_size, max_size, FUNC_SIZE])} байт'
    # return f'Число {num} встречается чаще всего - {max_} раз/раза'


print(count_max_1(lst_2))


# count_max_1 занимает 88632 байт -- с учётом lst_size

# Вычисляем сколько памяти занимает count_max_1
# dict_size - 640 байт
# lst_size - 87616 байт
# dict_lst_size - 184 байт
# num_size - 28 байт
# max_size - 28 байт
# count_max_1 занимает 1016 байт -- без lst_size

def count_max_2(lst: list):
    print('*' * 95)
    print('Вычисляем сколько памяти занимает count_max_2')
    array = []
    for itm in lst:
        # array.append((itm, lst.count(itm)))
        array = [(itm, lst.count(itm))]
    array = list(set(array))

    max_amount = 0
    num = None
    for obj in array:
        if obj[1] > max_amount:
            max_amount = obj[1]
            num = obj[0]
    lst_size = getsizeof(lst)
    array_size = getsizeof(array)
    max_amount_size = getsizeof(max_amount)
    num_size = getsizeof(num)
    print(f'lst_size - {lst_size} байт')
    print(f'array_size - {array_size} байт')
    print(f'max_amount_size - {max_amount_size} байт')
    print(f'num_size - {num_size} байт')
    # return f'count_max_2 занимает {sum([lst_size,array_size, max_amount_size, num_size, FUNC_SIZE])} байт'
    return f'count_max_2 занимает {sum([array_size, max_amount_size, num_size, FUNC_SIZE])} байт'
    # return f'Число {num} встречается чаще всего - {max_amount} раз/раза'


print(count_max_2(lst_2))


# count_max_2 занимает 87872 байт -- с учётом lst_size

# Вычисляем сколько памяти занимает count_max_2
# lst_size - 87616 байт
# array_size - 64 байт
# max_amount_size - 28 байт
# num_size - 28 байт
# count_max_2 занимает 256 байт -- без lst_size


def count_max_3(lst: list):
    print('*' * 95)
    print('Вычисляем сколько памяти занимает count_max_3')
    num = lst[0]
    frequency = 1
    for i in range(len(lst)):
        spam = 1
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                spam += 1
        if spam > frequency:
            frequency = spam
            num = lst[i]
    num_size = getsizeof(num)
    frequency_size = getsizeof(frequency)
    lst_size = getsizeof(lst)
    print(f'num_size - {num_size} байт')
    print(f'frequency_size - {frequency_size} байт')
    print(f'lst_size - {lst_size} байт')
    # return f'count_max_3 занимает {sum([lst_size, num_size, frequency_size, FUNC_SIZE])} байт'
    return f'count_max_3 занимает {sum([num_size, frequency_size, FUNC_SIZE])} байт'
    # return f'Число {num} встречается {frequency} раз(а)' if frequency > 1 else 'Все элементы уникальны'


print(count_max_3(lst_2))


# count_max_3 занимает 87808 байт -- с учётом lst_size

# Вычисляем сколько памяти занимает count_max_3
# num_size - 28 байт
# frequency_size - 28 байт
# lst_size - 87616 байт
# count_max_3 занимает 192 байт -- без lst_size


def count_max_4(lst: list):
    print('*' * 95)
    print('Вычисляем сколько памяти занимает count_max_4')
    counter = {}
    frequency = 1
    num = None
    for itm in lst:
        if itm in counter:
            counter[itm] += 1
        else:
            counter[itm] = 1

        if frequency < counter[itm]:
            frequency = counter[itm]
            num = itm
    counter_size = getsizeof(counter)
    lst_size = getsizeof(lst)
    num_size = getsizeof(num)
    frequency_size = getsizeof(frequency)
    print(f'counter_size - {counter_size}')
    print(f'lst_size - {lst_size}')
    print(f'num_size - {num_size}')
    print(f'frequency_size - {frequency_size}')
    # return f'count_max_4 занимает {sum([lst_size, counter_size, num_size, frequency_size, FUNC_SIZE])} байт'
    return f'count_max_4 занимает {sum([counter_size, num_size, frequency_size, FUNC_SIZE])} байт'
    # return f'Число {num} встречается {frequency} раз(а)'


print(count_max_4(lst_2))
# count_max_4 занимает 88448 байт -- с учётом lst_size

# Вычисляем сколько памяти занимает count_max_4
# counter_size - 640
# lst_size - 87616
# num_size - 28
# frequency_size - 28
# count_max_4 занимает 832 байт -- без lst_size

'''
Большую часть памяти занимают входные данные. Если не учитывать их (lst_size), то решения реализованные через словари 
занимают больше места из-за того что хэш занимает много памяти. А вот решения с помощью списков занимает меньше места.
Итог: Список занимает меньше памяти, но её сложность будет квадратичной из-за вложенного цикла. 
А код реализованный с помощью словаря будет работать быстрее потому мы проверяем наличие элемента во время итерации
что избавляет нас от необходимости использовать вложенные циклы. Не смотря на занимаемую память, решение с помощью 
словарей будет работать эффективней, да и разница в памяти не такая уж и критичная для современных процессоров
'''
