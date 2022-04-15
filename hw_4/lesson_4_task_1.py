"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.

Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом
  (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

# 4-я задача 3-го урока
# Определить, какое число в массиве встречается чаще всего.
import timeit
import cProfile
from random import randint

dictionary = {}
lst_0 = [randint(1, 15) for _ in range(10)]
lst_1 = [randint(1, 15) for _ in range(100)]
lst_2 = [randint(1, 15) for _ in range(1000)]
lst_3 = [randint(1, 15) for _ in range(10_000)]
lst_4 = [randint(1, 15) for _ in range(100_000)]
lst_5 = [randint(1, 15) for _ in range(1000_000)]


def count_max_1(lst: list):
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
    return f'Число {num} встречается чаще всего - {max_} раз/раза'


# # Замер списка с 10 элементами
# print(timeit.timeit('count_max_1(lst_0)', number=1000, globals=globals()))  # 0.0026918749999822467
# # Замер списка с 100 элементами
# print(timeit.timeit('count_max_1(lst_1)', number=1000, globals=globals()))  # 0.011934711999970204
# # Замер списка с 1000 элементами
# print(timeit.timeit('count_max_1(lst_2)', number=1000, globals=globals()))  # 0.09289151799998763
# # Замер списка с 10_000 элементами
# print(timeit.timeit('count_max_1(lst_3)', number=1000, globals=globals()))  # 0.9172121889999971
# # Замер списка с 100_000 элементами
# print(timeit.timeit('count_max_1(lst_4)', number=1000, globals=globals()))  # 9.154341623999926
# # Замер списка с 1000_000 элементами
# print(timeit.timeit('count_max_1(lst_5)', number=1000, globals=globals()))  # 91.32104193400005
# cProfile.run('count_max_1(lst_5)')

'''
         6 function calls in 0.097 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.097    0.097 <string>:1(<module>)
        1    0.097    0.097    0.097    0.097 lesson_4_task_1.py:29(count_max_1)
        1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:35(<listcomp>)
        1    0.000    0.000    0.097    0.097 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
'''


def count_max_2(lst: list):
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

    return f'Число {num} встречается чаще всего - {max_amount} раз/раза'


# # Замер списка с 10 элементами
# print(timeit.timeit('count_max_2(lst_0)', number=1000, globals=globals()))  # 0.0020571519999066368
# # Замер списка с 100 элементами
# print(timeit.timeit('count_max_2(lst_1)', number=1000, globals=globals()))  # 0.06671929300500778
# # Замер списка с 1000 элементами
# print(timeit.timeit('count_max_2(lst_2)', number=1000, globals=globals()))  # 10.053342446997704
# # Замер списка с 10_000 элементами
# print(timeit.timeit('count_max_2(lst_3)', number=1000, globals=globals()))  # 1325.6559717779965
# # Замер списка с 100_000 элементами
# # Как вы можете видеть предыдущий замер занял 22 минуты. а чтобы вычислить следующий замер потребовалось бы в
# # 132,5 раза больше времени
# print(timeit.timeit('count_max_2(lst_4)', number=1000, globals=globals()))
# # Замер списка с 1000_000 элементами
# print(timeit.timeit('count_max_2(lst_5)', number=1000, globals=globals()))
# cProfile.run('count_max_2(lst_4)')

'''
         200004 function calls in 134.201 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  134.201  134.201 <string>:1(<module>)
        1    0.060    0.060  134.201  134.201 lesson_4_task_1.py:76(count_max_2)
        1    0.000    0.000  134.201  134.201 {built-in method builtins.exec}
   100000    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
   100000  134.135    0.001  134.135    0.001 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


def count_max_3(lst: list):
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

    return f'Число {num} встречается {frequency} раз(а)' if frequency > 1 else 'Все элементы уникальны'


# # Замер списка с 10 элементами
# print(timeit.timeit('count_max_3(lst_0)', number=1000, globals=globals()))  # 0.0038709569998900406
# # Замер списка с 100 элементами
# print(timeit.timeit('count_max_3(lst_1)', number=1000, globals=globals()))  # 0.2577820839942433
# # Замер списка с 1000 элементами
# print(timeit.timeit('count_max_3(lst_2)', number=1000, globals=globals()))  # 29.808642903000873
# # Замер списка с 10_000 элементами
# print(timeit.timeit('count_max_3(lst_3)', number=1000, globals=globals()))
# # Замер списка с 100_000 элементами
# print(timeit.timeit('count_max_3(lst_4)', number=1000, globals=globals()))
# # Замер списка с 1000_000 элементами
# print(timeit.timeit('count_max_3(lst_5)', number=1000, globals=globals()))
# cProfile.run('count_max_3(lst_4)')

'''
         100005 function calls in 318.838 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  318.838  318.838 <string>:1(<module>)
        1  318.832  318.832  318.838  318.838 lesson_4_task_1.py:121(count_max_3)
        1    0.000    0.000  318.838  318.838 {built-in method builtins.exec}
   100001    0.005    0.000    0.005    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


def count_max_4(lst: list):
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
    return f'Число {num} встречается {frequency} раз(а)'


# # Замер списка с 10 элементами
# print(timeit.timeit('count_max_4(lst_0)', number=1000, globals=globals()))  # 0.0010102729999061921
# # Замер списка с 100 элементами
# print(timeit.timeit('count_max_4(lst_1)', number=1000, globals=globals()))  # 0.011242413999980272
# # Замер списка с 1000 элементами
# print(timeit.timeit('count_max_4(lst_2)', number=1000, globals=globals()))  # 0.09780967300002885
# # Замер списка с 10_000 элементами
# print(timeit.timeit('count_max_4(lst_3)', number=1000, globals=globals()))  # 1.0031959259999894
# # Замер списка с 100_000 элементами
# print(timeit.timeit('count_max_4(lst_4)', number=1000, globals=globals()))  # 14.025072092999949
# # Замер списка с 1000_000 элементами
# print(timeit.timeit('count_max_4(lst_5)', number=1000, globals=globals()))  # 136.54285436099997
# cProfile.run('count_max_4(lst_5)')

'''
        4 function calls in 0.130 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.130    0.130 <string>:1(<module>)
        1    0.130    0.130    0.130    0.130 lesson_4_task_1.py:164(count_max_4)
        1    0.000    0.000    0.130    0.130 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
# print(count_max_1(lst_5))
# print(count_max_4(lst_5))
# print(count_max_2(lst_3))
# print(count_max_3(lst_3))

'''
Сложность алгоритма где задача реализована с помощью словаря (count_max_1 и count_max_4) - O(n) так как мы проходимся 
по n элементам, то есть линейная зависимость от количества вводных данных. Однако я не до конца понял почему ваша 
реализация (count_max_4) не работает одинаково, ведь его сложность схожа с моим решением (count_max_1). В начале думал 
что это из-за того что я вставил переменные внутри функции, но потом посмотрел ролик и понял что при оценке алгоритмы 
константы отсекаются, остаётся лишь n которая стремится к бесконечности. Был бы благодарен если бы объяснили почему 
так происходит. Сложность алгоритма функции count_max_2 - O(n + m) так как у нас есть метод count. А count_max_3 -
O(n^2) квадратичная из-за вложенного цикла.
'''

# Вывод: самый эффективный способ при больших объёмах данных это код реализованный через словари, а самый медленный
# способ это код реализованный через вложенные циклы.
