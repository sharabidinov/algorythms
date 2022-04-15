import timeit
import cProfile

"""
2). Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна
принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность
алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
Примечание. Вспомните классический способ проверки числа на простоту.
"""

# n_prime_num_input = int(input('Введите n-й элемент простого числа которую нужно вычислить: ')) # закомментировал
# чтобы не мешала при замерах

'''
Функция для идеального пользователя, который не будет искать не существующий элемент. Например если он в idx 
передал 15 То в n нужно передать число не превышающее 6-ти [2,3,5,7,11,13]. Попытался реализовать код с 
Решето Эратосфена где достаточно будет ввести n-й элемент, но не смог реализовать его(
Уверен есть способ где не надо вводить размер массива.
'''


def eratosthenes(idx, n):
    prime_list = [item for item in range(idx + 1)]
    prime_list[1] = 0
    index = 2

    while index <= idx:
        if prime_list[index] != 0:
            el = index * 2
            while el <= idx:
                prime_list[el] = 0
                el = el + index
        index += 1

    prime_list = list(set(prime_list))
    prime_list.sort()
    prime_list.remove(0)
    # print(prime_list)
    return prime_list[n - 1]


# print(timeit.timeit('eratosthenes(100, 10)', number=1000, globals=globals()))  # 0.013287162000779063
# print(timeit.timeit('eratosthenes(1000, 10)', number=1000, globals=globals()))  # 0.15517138900031568
# print(timeit.timeit('eratosthenes(10_000, 10)', number=1000, globals=globals()))  # 2.9823378840010264
# print(timeit.timeit('eratosthenes(100_000, 10)', number=1000, globals=globals()))  # 33.78098036799929
# print(timeit.timeit('eratosthenes(1000_000, 10)', number=1000, globals=globals()))  # 404.6601102780005
# print(timeit.timeit('eratosthenes(10_000_000, 10)', number=1000, globals=globals()))  # займёт ~ 12 раз больше времени
# cProfile.run('eratosthenes(10_000_000, 20_000)')

'''
         7 function calls in 3.486 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.023    0.023    3.486    3.486 <string>:1(<module>)
        1    3.162    3.162    3.463    3.463 lesson_4_task_2.py:26(eratosthenes)
        1    0.245    0.245    0.245    0.245 lesson_4_task_2.py:27(<listcomp>)
        1    0.000    0.000    3.486    3.486 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.001    0.001    0.001    0.001 {method 'remove' of 'list' objects}
        1    0.054    0.054    0.054    0.054 {method 'sort' of 'list' objects}
'''


def prime_n_element(n):
    num = 3
    prime_list = [2]

    if n == 1:
        return 2

    while len(prime_list) < n:
        for element in prime_list:
            if num % element == 0:
                break

        else:
            prime_list.append(num)

        num += 2

    return prime_list[-1]


# print(timeit.timeit('prime_n_element(20)', number=1000, globals=globals()))  # 0.009065436002856586
# print(timeit.timeit('prime_n_element(100)', number=1000, globals=globals()))  # 0.1575902340009634
# print(timeit.timeit('prime_n_element(200)', number=1000, globals=globals()))  # 0.7108014410005126
# print(timeit.timeit('prime_n_element(400)', number=1000, globals=globals()))  # 3.0286889739982144
# print(timeit.timeit('prime_n_element(800)', number=1000, globals=globals()))  # 12.834009324000363
# print(timeit.timeit('prime_n_element(1000)', number=1000, globals=globals()))  # 21.779639333999512
# print(cProfile.run('prime_n_element(20_000)'))

'''
         132372 function calls in 8.934 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    8.934    8.934 <string>:1(<module>)
        1    8.928    8.928    8.934    8.934 lesson_4_task_2.py:71(prime_n_element)
        1    0.000    0.000    8.934    8.934 {built-in method builtins.exec}
   112369    0.005    0.000    0.005    0.000 {built-in method builtins.len}
    19999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''


'''
Сложность алгоритма решета Эратосфена O(n log log n), которую можно отнести к линейно-логарифмической. Вторая задача
реализация имеет квадратичную сложность из-за вложенного цикла.
'''

# Вывод: код реализованный через решето Эратосфена эффективный, нежели моя реализация. Потому что моя реализация для
# вычисления 20 000 элемента простых чисел тратит 8.9 секунд, в то время как с решето Эратосфена с массивом в 10_000_000
# 20 000-й элемент находится за 3.7 секунд
# print(eratosthenes(300_000, 20_000))
# print(prime_n_element(20_000))
