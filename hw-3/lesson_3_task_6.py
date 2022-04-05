# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

lst = [1, 2, 3, 4]
max_index = 0
min_index = 0
max_num = 0
min_num = 0

for index in range(len(lst)):
    if lst[index] > lst[max_index]:
        max_index = index
        max_num = lst[max_index]
    elif lst[index] <= lst[min_index]:
        min_index = index
        min_num = lst[min_index]

sum_ = 0
for item in range(min_num+1, max_num):
    sum_ += item

print(sum_)
