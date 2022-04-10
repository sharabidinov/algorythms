# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа
# должна сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю
# о невозможности деления на ноль, если он ввел его в качестве делителя.
while True:
    num_1 = int(input('Введите num_1: '))
    num_2 = int(input('Введите num_2: '))
    operator = input('Введите оператор: ')
    operator_list = '+-*/'

    if operator == '0':
        break

    for item in operator_list:
        if item == operator:
            if num_2 == 0:
                print('Нельзя делить на 0')
                continue

            else:
                if item == '-':
                    calculation = num_1 - num_2
                    print(calculation)
                elif item == '+':
                    calculation = num_1 + num_2
                    print(calculation)
                elif item == '*':
                    calculation = num_1 * num_2
                    print(calculation)
                elif item == '/':
                    calculation = num_1 / num_2
                    print(calculation)


