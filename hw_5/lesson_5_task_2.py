"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число
представляется как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить
их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’,
‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import Counter

# Можете вводить в нижне регистре, программа отработает правильно
operand_1 = input('Введите перове шестнадцатеричное число: ')
operand_2 = input('Введите второе шестнадцатеричное число: ')

lst_1 = [_ for _ in operand_1.upper()]
lst_2 = [_ for _ in operand_2.upper()]

hexadecimal = Counter({
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15
})


def to_decimal(data: list):
    power = len(data) - 1
    decimal = 0

    for digit in data:
        decimal += hexadecimal[digit] * 16 ** power
        power -= 1

    return str(decimal)


def to_hexadecimal(data: str):
    hexadec = Counter({
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': 'A',
        '11': 'B',
        '12': 'C',
        '13': 'D',
        '14': 'E',
        '15': 'F'
    })

    hexa = int(data)
    remainder = []
    result = []
    while hexa != 0:
        remainder.append(hexa % 16)
        hexa = (hexa - (hexa % 16)) // 16

    for n in remainder:
        result.append(hexadec[str(n)])
    return result[::-1]


if __name__ == '__main__':
    sum_hexa = int(to_decimal(lst_1)) + int(to_decimal(lst_2))
    print(f'Сложение {lst_1} + {lst_2} = {to_hexadecimal(sum_hexa)}')
    multiply = int(to_decimal(lst_1)) * int(to_decimal(lst_2))
    print(f'Произведение {lst_1} * {lst_2} = {to_hexadecimal(multiply)}')
