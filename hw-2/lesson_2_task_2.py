# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# digit = int(input('Введите число: '))
#
# str_digit = str(digit)
# even = ''
# odd = ''
#
# for num in str_digit:
#     if int(num) % 2 == 0:
#         even += num
#     else:
#         odd += num
#
# print(f'количество четных цифр {len(even)}\n количество нечетных цифр {len(odd)}')

def count_odd_even(n: int, odd=0, even=0):
    if n == 0:
        return f'количество четных цифр {even}\nколичество нечетных цифр {odd}'

    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
    return count_odd_even(n, odd, even)


if __name__ == '__main__':
    num = int(input('введите число: '))
    print(count_odd_even(num))
